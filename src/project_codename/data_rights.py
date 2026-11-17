"""Fail-closed data provenance and use-entitlement contracts.

This module records administrative entitlement evidence supplied by an
authorized operator. It does not interpret provider contracts or infer rights
from successful data acquisition.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum

from .temporal import ensure_utc_datetime


class DataUse(StrEnum):
    INTERNAL = "internal"
    DISPLAY = "display"
    DERIVED = "derived"
    REDISTRIBUTION = "redistribution"


@dataclass(frozen=True, slots=True)
class DataEntitlement:
    """Rights scope for one acquired dataset and a bounded entitlement term."""

    entitlement_id: str
    provider: str
    dataset: str
    acquired: bool
    permitted_uses: frozenset[DataUse]
    effective_from: datetime
    effective_to: datetime | None
    evidence_uri: str | None
    approved_by: str | None

    def __post_init__(self) -> None:
        for field_name in ("entitlement_id", "provider", "dataset"):
            value = getattr(self, field_name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field_name} is required")
        if not isinstance(self.acquired, bool):
            raise TypeError("acquired must be a bool")
        if not isinstance(self.permitted_uses, frozenset) or any(
            not isinstance(use, DataUse) for use in self.permitted_uses
        ):
            raise TypeError("permitted_uses must be a frozenset of DataUse values")
        ensure_utc_datetime(self.effective_from, "effective_from")
        if self.effective_to is not None:
            ensure_utc_datetime(self.effective_to, "effective_to")
            if self.effective_to <= self.effective_from:
                raise ValueError("effective_to must be later than effective_from")
        if self.evidence_uri is not None and not self.evidence_uri.strip():
            raise ValueError("evidence_uri cannot be blank")
        if self.approved_by is not None and not self.approved_by.strip():
            raise ValueError("approved_by cannot be blank")


def authorize_data_use(
    entitlement: DataEntitlement | None,
    *,
    provider: str,
    dataset: str,
    use: DataUse,
    at: datetime,
) -> bool:
    """Return True only for acquired, evidenced, current, explicitly allowed use."""

    ensure_utc_datetime(at, "at")
    if not isinstance(use, DataUse):
        raise TypeError("use must be a DataUse")
    if entitlement is None or not entitlement.acquired:
        return False
    if entitlement.provider != provider or entitlement.dataset != dataset:
        return False
    if entitlement.evidence_uri is None or entitlement.approved_by is None:
        return False
    if at < entitlement.effective_from:
        return False
    if entitlement.effective_to is not None and at >= entitlement.effective_to:
        return False
    return use in entitlement.permitted_uses
