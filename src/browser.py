"""Playwright browser adapter for permitted HTML pages."""

from __future__ import annotations

from pathlib import Path

from playwright.async_api import async_playwright


async def fetch_html(url: str, *, headless: bool = True, timeout_ms: int = 30000) -> str:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=headless)
        try:
            page = await browser.new_page()
            await page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
            return await page.content()
        finally:
            await browser.close()


async def fetch_fixture(path: str | Path) -> str:
    absolute = Path(path).resolve()
    return await fetch_html(absolute.as_uri(), headless=True)
