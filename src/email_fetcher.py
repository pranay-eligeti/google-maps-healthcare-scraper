"""Extract public contact emails from provider webpages."""

from __future__ import annotations

import re
from typing import Iterable

EMAIL_RE = re.compile(r"\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}\\b", re.I)


def extract_emails(html: str) -> list[str]:
    found = {match.group(0).lower() for match in EMAIL_RE.finditer(html)}
    return sorted(found)


def first_public_email(html: str, excluded_domains: Iterable[str] = ()) -> str:
    excluded = {domain.lower().lstrip("@") for domain in excluded_domains}
    for email in extract_emails(html):
        if email.rsplit("@", 1)[-1] not in excluded:
            return email
    return ""
