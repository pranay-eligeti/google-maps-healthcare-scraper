from pathlib import Path

from src.cleaner import normalize_listing, normalize_phone
from src.email_fetcher import extract_emails
from src.parser import parse_listing_html

ROOT = Path(__file__).resolve().parents[1]


def test_fixture_browser_export_never_visits_provider_pages(monkeypatch, tmp_path):
    import asyncio
    import pandas as pd
    from src import main
    from src.exporter import export_csv

    async def forbidden(*args, **kwargs):
        raise AssertionError("Fixture mode must not visit external provider pages")

    monkeypatch.setattr(main, "fetch_html", forbidden)
    records = asyncio.run(main.scrape(str(ROOT / "sample_data/search_results.html"), fixture=True, headless=True, timeout_ms=30000))
    assert len(records) == 2 and records[1]["email"] == ""
    output = export_csv(records, tmp_path / "output.csv")
    assert len(pd.read_csv(output)) == 2


def test_parse_synthetic_fixture():
    html = (ROOT / "sample_data" / "search_results.html").read_text(encoding="utf-8")
    records = parse_listing_html(html)
    assert len(records) == 2
    assert records[0]["name"] == "Lakeview Cardiology"
    assert records[1]["state"] == "OH"


def test_normalize_listing():
    record = normalize_listing(
        {
            "name": "  Northstar   Pediatrics ",
            "address": "300 Example St",
            "phone": "1 (614) 555-0103",
            "email": " HELLO@EXAMPLE.COM ",
            "specialty": " Pediatrics ",
            "state": "oh",
            "source_url": "https://example.com/northstar",
        }
    )
    assert record["name"] == "Northstar Pediatrics"
    assert record["phone"] == "(614) 555-0103"
    assert record["email"] == "hello@example.com"
    assert record["state"] == "OH"


def test_invalid_phone_normalizes_to_empty():
    assert normalize_phone("123") == ""


def test_extract_emails_normalizes_and_deduplicates():
    html = "<p>Contact A@Example.com or a@example.com</p>"
    assert extract_emails(html) == ["a@example.com"]
