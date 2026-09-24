from pathlib import Path

from src.cleaner import normalize_listing, normalize_phone
from src.email_fetcher import extract_emails
from src.parser import parse_listing_html

ROOT = Path(__file__).resolve().parents[1]


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
