"""Text and record normalization helpers."""

from __future__ import annotations

import re
import unicodedata
from typing import Any


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = unicodedata.normalize("NFKC", str(value))
    return " ".join(text.strip().split())


def normalize_phone(value: Any) -> str:
    digits = re.sub(r"\\D+", "", normalize_text(value))
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    if len(digits) != 10:
        return ""
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"


def normalize_email(value: Any) -> str:
    return normalize_text(value).lower()


def normalize_listing(record: dict[str, Any]) -> dict[str, str]:
    return {
        "name": normalize_text(record.get("name")),
        "address": normalize_text(record.get("address")),
        "phone": normalize_phone(record.get("phone")),
        "email": normalize_email(record.get("email")),
        "specialty": normalize_text(record.get("specialty")),
        "state": normalize_text(record.get("state")).upper(),
        "source_url": normalize_text(record.get("source_url")),
    }
