from __future__ import annotations

import sys
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from project_codename.data_rights import (  # noqa: E402
    DataEntitlement,
    DataUse,
    authorize_data_use,
)


UTC = timezone.utc
START = datetime(2026, 11, 17, 12, tzinfo=UTC)


def entitlement(**overrides: object) -> DataEntitlement:
    values: dict[str, object] = {
        "entitlement_id": "contract:test-1",
        "provider": "fixture-provider",
        "dataset": "fixture-bars",
        "acquired": True,
        "permitted_uses": frozenset({DataUse.INTERNAL, DataUse.DERIVED}),
        "effective_from": START,
        "effective_to": START + timedelta(days=30),
        "evidence_uri": "https://example.invalid/contract",
        "approved_by": "owner-fixture",
    }
    values.update(overrides)
    return DataEntitlement(**values)  # type: ignore[arg-type]


class DataRightsTests(unittest.TestCase):
    def test_missing_or_unacquired_entitlement_fails_closed(self) -> None:
        self.assertFalse(authorize_data_use(None, provider="fixture-provider", dataset="fixture-bars", use=DataUse.INTERNAL, at=START))
        self.assertFalse(authorize_data_use(entitlement(acquired=False), provider="fixture-provider", dataset="fixture-bars", use=DataUse.INTERNAL, at=START))

    def test_requires_matching_provider_dataset_and_explicit_use(self) -> None:
        value = entitlement()
        self.assertTrue(authorize_data_use(value, provider="fixture-provider", dataset="fixture-bars", use=DataUse.INTERNAL, at=START))
        self.assertFalse(authorize_data_use(value, provider="other", dataset="fixture-bars", use=DataUse.INTERNAL, at=START))
        self.assertFalse(authorize_data_use(value, provider="fixture-provider", dataset="other", use=DataUse.INTERNAL, at=START))
        self.assertFalse(authorize_data_use(value, provider="fixture-provider", dataset="fixture-bars", use=DataUse.DISPLAY, at=START))

    def test_missing_evidence_or_approver_fails_closed(self) -> None:
        for value in (entitlement(evidence_uri=None), entitlement(approved_by=None)):
            self.assertFalse(authorize_data_use(value, provider="fixture-provider", dataset="fixture-bars", use=DataUse.INTERNAL, at=START))

    def test_entitlement_is_inclusive_at_start_and_exclusive_at_end(self) -> None:
        value = entitlement()
        self.assertTrue(authorize_data_use(value, provider="fixture-provider", dataset="fixture-bars", use=DataUse.INTERNAL, at=START))
        self.assertFalse(authorize_data_use(value, provider="fixture-provider", dataset="fixture-bars", use=DataUse.INTERNAL, at=value.effective_to))

    def test_rejects_invalid_interval_and_untyped_use(self) -> None:
        with self.assertRaisesRegex(ValueError, "later than effective_from"):
            entitlement(effective_to=START)
        with self.assertRaisesRegex(TypeError, "DataUse"):
            authorize_data_use(entitlement(), provider="fixture-provider", dataset="fixture-bars", use="internal", at=START)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
