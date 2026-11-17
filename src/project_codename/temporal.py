"""Shared timestamp validation for point-in-time domain records."""

from datetime import datetime


def ensure_utc_datetime(value: datetime, field_name: str) -> None:
    """Reject naive or non-UTC timestamps at domain boundaries."""

    if not isinstance(value, datetime):
        raise TypeError(f"{field_name} must be a datetime")
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{field_name} must be timezone-aware")
    if value.utcoffset().total_seconds() != 0:
        raise ValueError(f"{field_name} must use UTC")
