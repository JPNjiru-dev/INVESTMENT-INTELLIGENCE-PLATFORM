from __future__ import annotations

import sys
import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from project_codename.instruments import (  # noqa: E402
    AssetClass,
    EvidenceReference,
    InstrumentKind,
    InstrumentRecord,
    InstrumentSpecification,
)


UTC = timezone.utc
NOW = datetime(2026, 11, 17, 12, 0, tzinfo=UTC)


def evidence() -> EvidenceReference:
    return EvidenceReference(
        uri="https://example.invalid/spec",
        publisher="Fixture publisher",
        retrieved_at=NOW,
    )


def record(**overrides: object) -> InstrumentRecord:
    values: dict[str, object] = {
        "instrument_id": "fixture:spot:gold-usd",
        "kind": InstrumentKind.SPOT,
        "asset_class": AssetClass.COMMODITY,
        "symbol": "GOLDUSD",
        "name": "Fixture gold spot instrument",
        "provider": "fixture-provider",
        "quote_currency": "USD",
        "base_currency": "XAU",
        "valid_from": NOW,
        "evidence": evidence(),
    }
    values.update(overrides)
    return InstrumentRecord(**values)  # type: ignore[arg-type]


class InstrumentRecordTests(unittest.TestCase):
    def test_accepts_source_bound_spot_commodity_without_claiming_verified_specs(self) -> None:
        instrument = record()
        self.assertEqual(instrument.kind, InstrumentKind.SPOT)
        self.assertEqual(instrument.asset_class, AssetClass.COMMODITY)
        self.assertIsNone(instrument.specification.price_tick)

    def test_all_instrument_kinds_are_distinct(self) -> None:
        self.assertEqual(
            {kind.value for kind in InstrumentKind},
            {"spot", "cfd", "future", "equity", "etf", "index"},
        )

    def test_enforces_kind_and_asset_class_for_equity_etf_and_index(self) -> None:
        cases = (
            (InstrumentKind.EQUITY, AssetClass.INDEX),
            (InstrumentKind.ETF, AssetClass.EQUITY),
            (InstrumentKind.INDEX, AssetClass.ETF),
        )
        for kind, asset_class in cases:
            with self.subTest(kind=kind):
                with self.assertRaises(ValueError):
                    record(kind=kind, asset_class=asset_class)

    def test_rejects_naive_validity_timestamps(self) -> None:
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            record(valid_from=datetime(2026, 11, 17, 12, 0))

    def test_rejects_non_utc_aware_validity_timestamps(self) -> None:
        with self.assertRaisesRegex(ValueError, "must use UTC"):
            record(valid_from=datetime(2026, 11, 17, 15, 0, tzinfo=timezone(timedelta(hours=3))))

    def test_rejects_nonpositive_or_nonfinite_specification_values(self) -> None:
        for value in (Decimal("0"), Decimal("-0.01"), Decimal("NaN"), Decimal("Infinity")):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    InstrumentSpecification(price_tick=value)

    def test_rejects_binary_float_specification_values(self) -> None:
        with self.assertRaisesRegex(TypeError, "Decimal"):
            InstrumentSpecification(price_tick=0.01)  # type: ignore[arg-type]

    def test_rejects_empty_identity_fields(self) -> None:
        with self.assertRaisesRegex(ValueError, "provider is required"):
            record(provider=" ")

    def test_requires_specific_asset_class_for_spot_instruments(self) -> None:
        with self.assertRaisesRegex(ValueError, "spot instruments"):
            record(asset_class=AssetClass.EQUITY)

    def test_validity_interval_must_be_increasing(self) -> None:
        with self.assertRaisesRegex(ValueError, "later than valid_from"):
            record(valid_to=NOW)
        with self.assertRaisesRegex(ValueError, "later than valid_from"):
            record(valid_to=NOW - timedelta(seconds=1))

    def test_rejects_untyped_kind_values(self) -> None:
        with self.assertRaisesRegex(TypeError, "InstrumentKind"):
            record(kind="spot")

    def test_cfd_on_an_index_remains_a_cfd(self) -> None:
        instrument = record(
            instrument_id="provider-a:cfd:nas100",
            kind=InstrumentKind.CFD,
            asset_class=AssetClass.INDEX,
            symbol="NAS100",
            name="Provider-specific index CFD",
            base_currency=None,
        )
        self.assertEqual(instrument.kind, InstrumentKind.CFD)
        self.assertEqual(instrument.asset_class, AssetClass.INDEX)

    def test_crypto_is_an_asset_class_not_a_contract_kind(self) -> None:
        instrument = record(
            instrument_id="provider-a:spot:btc-usd",
            asset_class=AssetClass.CRYPTO,
            symbol="BTCUSD",
            name="Provider-specific spot crypto instrument",
            base_currency="BTC",
        )
        self.assertEqual(instrument.kind, InstrumentKind.SPOT)
        self.assertEqual(instrument.asset_class, AssetClass.CRYPTO)


if __name__ == "__main__":
    unittest.main()
