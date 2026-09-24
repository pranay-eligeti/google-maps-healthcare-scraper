"""Parse listing cards from HTML using explicit data attributes."""

from __future__ import annotations

from bs4 import BeautifulSoup


def _text(card, selector: str) -> str:
    node = card.select_one(selector)
    return node.get_text(" ", strip=True) if node else ""


def parse_listing_html(html: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    records: list[dict[str, str]] = []

    for card in soup.select("[data-listing]"):
        records.append(
            {
                "name": _text(card, "[data-name]"),
                "address": _text(card, "[data-address]"),
                "phone": _text(card, "[data-phone]"),
                "email": _text(card, "[data-email]"),
                "specialty": _text(card, "[data-specialty]"),
                "state": _text(card, "[data-state]"),
                "source_url": card.get("data-source-url", ""),
            }
        )

    return records
