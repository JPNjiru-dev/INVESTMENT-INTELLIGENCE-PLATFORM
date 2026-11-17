from __future__ import annotations

import sys
import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from project_codename.instruments import EvidenceReference  # noqa: E402
from project_codename.market_data import (  # noqa: E402
    BarObservation,
    BarState,
    final_bars_as_of,
)


UTC = timezone.utc
START = datetime(2026, 11, 17, 12, 0, tzinfo=UTC)
END = START + timedelta(hours=1)


def evidence() -> EvidenceReference:
    return EvidenceReference(
        uri="https://example.invalid/fixture",
        publisher="Synthetic test fixture",
        retrieved_at=START,
    )


def bar(**overrides: object) -> BarObservation:
    values: dict[str, object] = {
        "instrument_id": "fixture:future:index",
        "provider": "fixture-provider",
        "source_symbol": "TEST1!",
        "interval_start": START,
        "interval_end": END,
        "available_at": END,
        "recorded_at": END + timedelta(seconds=2),
        "open": Decimal("100"),
        "high": Decimal("110"),
        "low": Decimal("90"),
        "close": Decimal("105"),
        "volume": Decimal("25"),
        "evidence": evidence(),
    }
    values.update(overrides)
    return BarObservation(**values)  # type: ignore[arg-type]


class BarObservationTests(unittest.TestCase):
    def test_accepts_synthetic_final_bar_fixture(self) -> None:
        observation = bar()
        self.assertEqual(observation.state, BarState.FINAL)
        self.assertEqual(observation.available_at, END)

    def test_rejects_final_bar_available_before_interval_end(self) -> None:
        with self.assertRaisesRegex(ValueError, "before its interval ends"):
            bar(available_at=END - timedelta(microseconds=1))

    def test_rejects_recorded_time_before_source_availability(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot precede source availability"):
            bar(recorded_at=END - timedelta(seconds=1))

    def test_rejects_non_utc_or_naive_bar_timestamps(self) -> None:
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            bar(interval_start=datetime(2026, 11, 17, 12))
        with self.assertRaisesRegex(ValueError, "must use UTC"):
            bar(available_at=END.astimezone(timezone(timedelta(hours=3))))

    def test_rejects_invalid_ohlc_relationships(self) -> None:
        with self.assertRaisesRegex(ValueError, "low <= open/close <= high"):
            bar(high=Decimal("99"))
        with self.assertRaisesRegex(ValueError, "low cannot exceed high"):
            bar(low=Decimal("111"), high=Decimal("110"))

    def test_rejects_float_and_nonfinite_price_values(self) -> None:
        with self.assertRaisesRegex(TypeError, "Decimal"):
            bar(close=105.0)  # type: ignore[arg-type]
        with self.assertRaisesRegex(ValueError, "must be finite"):
            bar(close=Decimal("NaN"))

    def test_rejects_negative_volume_but_allows_zero_volume(self) -> None:
        with self.assertRaisesRegex(ValueError, "volume cannot be negative"):
            bar(volume=Decimal("-1"))
        self.assertEqual(bar(volume=Decimal("0")).volume, Decimal("0"))

    def test_allows_negative_prices(self) -> None:
        observation = bar(
            open=Decimal("-10"),
            high=Decimal("-5"),
            low=Decimal("-20"),
            close=Decimal("-12"),
        )
        self.assertLess(observation.close, Decimal("0"))

    def test_point_in_time_selection_excludes_future_revisions(self) -> None:
        original = bar()
        correction_time = END + timedelta(hours=2)
        correction = bar(
            available_at=correction_time,
            recorded_at=correction_time + timedelta(seconds=1),
            close=Decimal("103"),
            revision=2,
            source_revision_id="correction-2",
        )

        early = final_bars_as_of([original, correction], instrument_id=original.instrument_id, as_of=END)
        late = final_bars_as_of(
            [original, correction],
            instrument_id=original.instrument_id,
            as_of=correction_time,
        )
        self.assertEqual(early, [original])
        self.assertEqual(late, [correction])

    def test_point_in_time_selection_ignores_partial_and_other_instrument_bars(self) -> None:
        final = bar()
        partial = bar(
            instrument_id=final.instrument_id,
            state=BarState.PARTIAL,
            available_at=START + timedelta(minutes=5),
            recorded_at=START + timedelta(minutes=6),
        )
        other = bar(instrument_id="other:instrument")
        selected = final_bars_as_of(
            [final, partial, other],
            instrument_id=final.instrument_id,
            as_of=END + timedelta(days=1),
        )
        self.assertEqual(selected, [final])

    def test_point_in_time_result_is_sorted_by_interval(self) -> None:
        first = bar()
        second = bar(
            interval_start=END,
            interval_end=END + timedelta(hours=1),
            available_at=END + timedelta(hours=1),
            recorded_at=END + timedelta(hours=1, seconds=2),
        )
        selected = final_bars_as_of(
            [second, first],
            instrument_id=first.instrument_id,
            as_of=END + timedelta(hours=2),
        )
        self.assertEqual(selected, [first, second])

    def test_rejects_conflicting_same_time_revision_ids(self) -> None:
        original = bar()
        conflict = bar(close=Decimal("104"))
        with self.assertRaisesRegex(ValueError, "conflicting bar revisions"):
            final_bars_as_of(
                [original, conflict],
                instrument_id=original.instrument_id,
                as_of=END,
            )

    def test_rejects_multiple_provider_symbols_mapped_to_one_instrument_id(self) -> None:
        first = bar()
        other_source = bar(provider="provider-b", source_symbol="XAU/USD")
        with self.assertRaisesRegex(ValueError, "assign distinct instrument_id"):
            final_bars_as_of(
                [first, other_source],
                instrument_id=first.instrument_id,
                as_of=END,
            )

    def test_allows_same_display_symbol_as_distinct_instrument_ids(self) -> None:
        first = bar(instrument_id="provider-a:spot:xauusd", source_symbol="XAUUSD")
        second = bar(instrument_id="provider-b:cfd:xauusd", provider="provider-b", source_symbol="XAUUSD")
        self.assertEqual(final_bars_as_of([first, second], instrument_id=first.instrument_id, as_of=END), [first])
        self.assertEqual(final_bars_as_of([first, second], instrument_id=second.instrument_id, as_of=END), [second])

    def test_historical_replay_boundary_is_inclusive_for_revision_availability(self) -> None:
        original = bar()
        correction_time = END + timedelta(minutes=5)
        correction = bar(
            available_at=correction_time,
            recorded_at=correction_time + timedelta(seconds=1),
            close=Decimal("104"),
            revision=2,
        )
        self.assertEqual(final_bars_as_of([original, correction], instrument_id=original.instrument_id, as_of=correction_time - timedelta(microseconds=1)), [original])
        self.assertEqual(final_bars_as_of([original, correction], instrument_id=original.instrument_id, as_of=correction_time), [correction])

    def test_requires_utc_as_of_time_and_instrument_id(self) -> None:
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            final_bars_as_of([], instrument_id="x", as_of=datetime(2026, 11, 17, 13))
        with self.assertRaisesRegex(ValueError, "instrument_id is required"):
            final_bars_as_of([], instrument_id=" ", as_of=END)


if __name__ == "__main__":
    unittest.main()
