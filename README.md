# 🗺️ Healthcare Listing Acquisition & Browser Automation

> A sanitized, runnable Python + Playwright portfolio project demonstrating browser-based listing extraction, normalization, public contact discovery, and structured CSV export.

[![Python CI](https://github.com/pranay-eligeti/google-maps-healthcare-scraper/actions/workflows/ci.yml/badge.svg)](https://github.com/pranay-eligeti/google-maps-healthcare-scraper/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-browser%20automation-green)
![pandas](https://img.shields.io/badge/pandas-data%20processing-purple)

## What this repository demonstrates

I have used Python and browser automation for healthcare data acquisition and validation in professional work.

This repository is the **public, sanitized implementation of that engineering pattern**. It uses a synthetic HTML fixture for deterministic testing and contains no employer exports, PHI, credentials, internal URLs, or proprietary source code.

### Engineering capabilities

- Browser automation with **Playwright**
- Explicit HTML listing parsing
- Unicode/text normalization
- Phone and email normalization
- Best-effort public contact discovery
- Structured CSV export
- Unit tests
- GitHub Actions CI

## Architecture

~~~text
HTML page / synthetic fixture
          |
          v
      Playwright
          |
          v
   Listing card parser
          |
          v
   Record normalization
          |
          +------> provider page (optional)
          |                 |
          |                 v
          |          public email extraction
          |                 |
          +-----------------+
                    |
                    v
                CSV output
~~~

See docs/architecture.md for design notes.

## Repository structure

~~~text
google-maps-healthcare-scraper/
├── .github/workflows/ci.yml
├── docs/architecture.md
├── sample_data/search_results.html
├── src/
│   ├── browser.py
│   ├── cleaner.py
│   ├── email_fetcher.py
│   ├── exporter.py
│   ├── main.py
│   └── parser.py
├── tests/test_parser.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
~~~

## Quick start

### Install

~~~bash
git clone https://github.com/pranay-eligeti/google-maps-healthcare-scraper.git
cd google-maps-healthcare-scraper

python -m venv .venv

# Windows
.venv\\Scripts\\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium
~~~

### Run the deterministic demo

~~~bash
python -m src.main --fixture sample_data/search_results.html --output output/listings.csv --headless
~~~

Expected result: **2 synthetic listings** written to output/listings.csv.

### Run tests

~~~bash
pytest -q
~~~

## Output schema

| Field | Description |
| --- | --- |
| name | Listing/provider name |
| address | Normalized address |
| phone | Normalized phone number |
| email | Public contact email when available |
| specialty | Specialty/category |
| state | State code |
| source_url | Source/provider URL |

## Production-minded design

**Separation of concerns**  
Browser fetching, parsing, normalization, contact extraction, and export are separate modules.

**Deterministic testing**  
CI runs against a local synthetic fixture rather than depending on a third-party website.

**Recoverable failures**  
Provider-page contact discovery is best-effort. A failed contact page does not terminate the full batch.

**Configuration and secrets**  
Runtime values live outside source control. .env.example documents the expected configuration.

## Privacy and usage

Do not commit real healthcare records, PHI, private employer exports, credentials, or internal URLs.

The public implementation does **not** include anti-bot evasion, credential bypassing, or access-control circumvention. For live websites, use an approved API or permitted automation method and follow applicable terms and policies.

## Portfolio note

Professional healthcare acquisition systems can be substantially more complex than this public reference implementation. The purpose of this repository is to make the core engineering patterns **visible, reproducible, testable, and explainable** without publishing private business systems.

## Author

**Pranay Eligeti**

[LinkedIn](https://www.linkedin.com/in/pranay-eligeti) · [GitHub](https://github.com/pranay-eligeti)
