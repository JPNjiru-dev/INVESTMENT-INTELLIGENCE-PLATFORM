"""Point-in-time market observation contracts; no provider adapter is included."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from typing import Iterable

from .instruments import EvidenceReference
from .temporal import ensure_utc_datetime


class BarState(StrEnum):
    PARTIAL = "partial"
    FINAL = "final"


def _finite_decimal(value: Decimal, field_name: str) -> None:
    if not isinstance(value, Decimal):
        raise TypeError(f"{field_name} must be a Decimal; floats are not accepted")
    if not value.is_finite():
        raise ValueError(f"{field_name} must be finite")


@dataclass(frozen=True, slots=True)
class BarObservation:
    """One source revision of an OHLCV bar.

    available_at means the time this exact revision was available from the
    source to the entitled analysis context. recorded_at is when this system
    captured it. Historical replay must filter by available_at; recorded_at is
    provenance and must not be backdated to make data appear available sooner.
    """

    instrument_id: str
    provider: str
    source_symbol: str
    interval_start: datetime
    interval_end: datetime
    available_at: datetime
    recorded_at: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    evidence: EvidenceReference
    volume: Decimal | None = None
    state: BarState = BarState.FINAL
    revision: int = 1
    source_revision_id: str | None = None

    def __post_init__(self) -> None:
        for field_name in ("instrument_id", "provider", "source_symbol"):
            value = getattr(self, field_name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field_name} is required")
        if not isinstance(self.state, BarState):
            raise TypeError("state must be a BarState")
        if not isinstance(self.evidence, EvidenceReference):
            raise TypeError("evidence must be an EvidenceReference")

        for field_name in ("interval_start", "interval_end", "available_at", "recorded_at"):
            ensure_utc_datetime(getattr(self, field_name), field_name)
        if self.interval_end <= self.interval_start:
            raise ValueError("interval_end must be later than interval_start")
        if self.recorded_at < self.available_at:
            raise ValueError("recorded_at cannot precede source availability")
        if self.state is BarState.FINAL and self.available_at < self.interval_end:
            raise ValueError("a final bar cannot be available before its interval ends")

        for field_name in ("open", "high", "low", "close"):
            _finite_decimal(getattr(self, field_name), field_name)
        if self.low > self.high:
            raise ValueError("low cannot exceed high")
        if self.low > min(self.open, self.close) or self.high < max(self.open, self.close):
            raise ValueError("bar prices must satisfy low <= open/close <= high")
        if self.volume is not None:
            _finite_decimal(self.volume, "volume")
            if self.volume < 0:
                raise ValueError("volume cannot be negative")
        if isinstance(self.revision, bool) or not isinstance(self.revision, int) or self.revision < 1:
            raise ValueError("revision must be a positive integer")
        if self.source_revision_id is not None and not self.source_revision_id.strip():
            raise ValueError("source_revision_id cannot be blank")


def final_bars_as_of(
    observations: Iterable[BarObservation],
    *,
    instrument_id: str,
    as_of: datetime,
) -> list[BarObservation]:
    """Return the latest source-available final revision of each interval.

    This enforces timestamp selection only. Callers still must establish that
    the source timestamp is trustworthy and that the user had appropriate
    entitlements for the historical period.
    """

    ensure_utc_datetime(as_of, "as_of")
    if not instrument_id.strip():
        raise ValueError("instrument_id is required")

    by_interval: dict[tuple[object, object], list[BarObservation]] = {}
    for observation in observations:
        if observation.instrument_id != instrument_id or observation.state is not BarState.FINAL:
            continue
        if observation.available_at > as_of:
            continue
        key = (observation.interval_start, observation.interval_end)
        by_interval.setdefault(key, []).append(observation)

    selected: list[BarObservation] = []
    for interval, revisions in by_interval.items():
        latest_key = max((item.available_at, item.revision) for item in revisions)
        latest = [
            item for item in revisions
            if (item.available_at, item.revision) == latest_key
        ]
        if any(item != latest[0] for item in latest[1:]):
            raise ValueError(f"conflicting bar revisions for interval {interval!r}")
        selected.append(latest[0])
    return sorted(selected, key=lambda item: item.interval_start)
