"""Provider-neutral instrument identity and specification contracts.

These records describe an instrument and its source-specific conventions. They
do not represent prices, imply that specifications are complete, or establish
market-data rights.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from enum import StrEnum

from .temporal import ensure_utc_datetime

class InstrumentKind(StrEnum):
    SPOT = "spot"
    CFD = "cfd"
    FUTURE = "future"
    EQUITY = "equity"
    ETF = "etf"
    INDEX = "index"


class AssetClass(StrEnum):
    FOREX = "forex"
    COMMODITY = "commodity"
    EQUITY = "equity"
    ETF = "etf"
    INDEX = "index"
    CRYPTO = "crypto"
    BOND = "bond"
    RATE = "rate"
    OTHER = "other"


def _positive_decimal(value: Decimal | None, field_name: str) -> None:
    if value is None:
        return
    if not isinstance(value, Decimal):
        raise TypeError(f"{field_name} must be a Decimal; floats are not accepted")
    if not value.is_finite() or value <= 0:
        raise ValueError(f"{field_name} must be finite and greater than zero")


@dataclass(frozen=True, slots=True)
class EvidenceReference:
    """Provenance for a fact about an instrument or its conventions."""

    uri: str
    publisher: str
    retrieved_at: datetime
    published_at: datetime | None = None
    note: str | None = None

    def __post_init__(self) -> None:
        if not self.uri.strip():
            raise ValueError("evidence uri is required")
        if not self.publisher.strip():
            raise ValueError("evidence publisher is required")
        ensure_utc_datetime(self.retrieved_at, "retrieved_at")
        if self.published_at is not None:
            ensure_utc_datetime(self.published_at, "published_at")


@dataclass(frozen=True, slots=True)
class InstrumentSpecification:
    """Provider/venue-specific trading conventions; unknown fields stay absent."""

    price_tick: Decimal | None = None
    quantity_step: Decimal | None = None
    contract_multiplier: Decimal | None = None
    settlement_currency: str | None = None
    quantity_unit: str | None = None

    def __post_init__(self) -> None:
        _positive_decimal(self.price_tick, "price_tick")
        _positive_decimal(self.quantity_step, "quantity_step")
        _positive_decimal(self.contract_multiplier, "contract_multiplier")
        if self.settlement_currency is not None and not self.settlement_currency.strip():
            raise ValueError("settlement_currency cannot be blank")
        if self.quantity_unit is not None and not self.quantity_unit.strip():
            raise ValueError("quantity_unit cannot be blank")


_REQUIRED_KIND_CLASS: dict[InstrumentKind, AssetClass] = {
    InstrumentKind.EQUITY: AssetClass.EQUITY,
    InstrumentKind.ETF: AssetClass.ETF,
    InstrumentKind.INDEX: AssetClass.INDEX,
}


@dataclass(frozen=True, slots=True)
class InstrumentRecord:
    """A source-bound instrument identity effective over a time interval.

    Symbols are not globally unique. Provider plus symbol and optional venue
    identify the source instrument; instrument_id is the stable internal key.
    Evidence records provenance but this type does not verify specification
    correctness or the source's legal data-use terms.
    """

    instrument_id: str
    kind: InstrumentKind
    asset_class: AssetClass
    symbol: str
    name: str
    provider: str
    quote_currency: str
    valid_from: datetime
    evidence: EvidenceReference
    venue: str | None = None
    base_currency: str | None = None
    specification: InstrumentSpecification = InstrumentSpecification()
    valid_to: datetime | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.kind, InstrumentKind):
            raise TypeError("kind must be an InstrumentKind")
        if not isinstance(self.asset_class, AssetClass):
            raise TypeError("asset_class must be an AssetClass")
        if not isinstance(self.evidence, EvidenceReference):
            raise TypeError("evidence must be an EvidenceReference")
        if not isinstance(self.specification, InstrumentSpecification):
            raise TypeError("specification must be an InstrumentSpecification")
        for field_name in ("instrument_id", "symbol", "name", "provider", "quote_currency"):
            if not getattr(self, field_name).strip():
                raise ValueError(f"{field_name} is required")

        required_class = _REQUIRED_KIND_CLASS.get(self.kind)
        if required_class is not None and self.asset_class is not required_class:
            raise ValueError(f"{self.kind.value} instruments must use {required_class.value} asset class")
        if self.kind is InstrumentKind.SPOT and self.asset_class not in {
            AssetClass.FOREX,
            AssetClass.COMMODITY,
            AssetClass.CRYPTO,
        }:
            raise ValueError("spot instruments must be forex, commodity, or crypto assets")

        ensure_utc_datetime(self.valid_from, "valid_from")
        if self.valid_to is not None:
            ensure_utc_datetime(self.valid_to, "valid_to")
            if self.valid_to <= self.valid_from:
                raise ValueError("valid_to must be later than valid_from")

        if self.base_currency is not None and not self.base_currency.strip():
            raise ValueError("base_currency cannot be blank")


def utc_now() -> datetime:
    """Return an aware UTC timestamp for evidence capture."""

    return datetime.now(timezone.utc)
