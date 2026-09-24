"""CLI for the public healthcare listing acquisition demo."""

from __future__ import annotations

import argparse
import asyncio
import os
from pathlib import Path

from .browser import fetch_fixture, fetch_html
from .cleaner import normalize_listing
from .email_fetcher import first_public_email
from .exporter import export_csv
from .parser import parse_listing_html


async def scrape(url_or_path: str, *, fixture: bool, headless: bool, timeout_ms: int) -> list[dict[str, str]]:
    html = (
        await fetch_fixture(url_or_path)
        if fixture
        else await fetch_html(url_or_path, headless=headless, timeout_ms=timeout_ms)
    )
    records = [normalize_listing(item) for item in parse_listing_html(html)]

    for record in records:
        if not record["email"] and record["source_url"]:
            try:
                provider_html = await fetch_html(
                    record["source_url"], headless=headless, timeout_ms=timeout_ms
                )
                record["email"] = first_public_email(provider_html)
            except Exception:
                record["email"] = ""

    return records


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract structured listing data from HTML.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--fixture", help="Local HTML fixture path")
    source.add_argument("--url", help="Permitted webpage URL")
    parser.add_argument("--output", default=os.getenv("OUTPUT_DIR", "./output") + "/listings.csv")
    parser.add_argument("--headless", action="store_true", help="Run Playwright headless")
    parser.add_argument("--timeout-ms", type=int, default=int(os.getenv("REQUEST_TIMEOUT_MS", "30000")))
    return parser


def main() -> None:
    args = build_parser().parse_args()
    records = asyncio.run(
        scrape(
            args.fixture or args.url,
            fixture=bool(args.fixture),
            headless=args.headless,
            timeout_ms=args.timeout_ms,
        )
    )
    output = export_csv(records, Path(args.output))
    print(f"Extracted {len(records)} listings -> {output}")


if __name__ == "__main__":
    main()
