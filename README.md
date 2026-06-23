# 🗺️ Google Maps Healthcare Data Scraper

> A GUI-based Python scraper that collects healthcare provider data (names, addresses, phones, emails) from Google Maps at scale — with anti-bot bypass, parallel email fetching, and Google Places validation.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![tkinter](https://img.shields.io/badge/tkinter-GUI-lightgrey)
![Google Places](https://img.shields.io/badge/Google%20Places-API-red?logo=google)

---

## What It Does

Automates large-scale collection of healthcare clinic and provider data from Google Maps — replacing hours of manual searching with a GUI-controlled scraper that runs quietly in the background, bypasses bot detection, and outputs clean, structured CSV files ready for outreach pipelines.

---

## Features

- ✅ **Anti-bot bypass** — uses `undetected-chromedriver` to avoid Google detection
- ✅ **tkinter GUI** — point-and-click interface, no command line needed for end users
- ✅ **Parallel email fetching** — fetches emails from provider websites concurrently for speed
- ✅ **Unicode normalization** — cleans non-ASCII characters in clinic and provider names
- ✅ **Google Places API validation** — verifies placeholder/Results rows using specialty keyword appending
- ✅ **Structured CSV output** — name, address, phone, email, specialty, state, source URL

---

## How It Works

```
User opens GUI (tkinter)
        │
        ▼
Selects: Specialty + State + Search Radius
        │
        ▼
Playwright + undetected-chromedriver launches browser
        │
        ▼
Searches Google Maps: "Urgent Care clinics in Columbus OH"
        │
        ├── Scrolls results, extracts listings
        ├── Clicks each listing → scrapes name, address, phone
        ├── Visits clinic website (if available) → parallel email fetch
        ├── Unicode-normalizes all text fields
        └── Validates against Google Places API (specialty keyword appended)
        │
        ▼
Exports clean CSV → feeds into Healthcare Lead Automation pipeline
```

---

## Tech Stack

| Tool                         | Purpose                             |
| ---------------------------- | ----------------------------------- |
| Python 3.10+                 | Core scraping logic                 |
| Playwright                   | Browser automation                  |
| undetected-chromedriver      | Anti-bot bypass for Google Maps     |
| tkinter                      | Desktop GUI for non-technical users |
| Google Places API            | Validation of scraped listings      |
| asyncio / ThreadPoolExecutor | Parallel email fetching             |
| pandas                       | Data cleaning and CSV export        |
| unicodedata                  | Unicode normalization               |

---

## Project Structure

```
google-maps-healthcare-scraper/
├── src/
│   ├── gui.py               # tkinter GUI entry point
│   ├── scraper.py           # Playwright scraping logic
│   ├── email_fetcher.py     # Parallel email extraction
│   ├── places_validator.py  # Google Places API validation
│   ├── cleaner.py           # Unicode normalization + formatting
│   └── exporter.py          # CSV output
├── .env.example
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/pranay-eligeti/google-maps-healthcare-scraper.git
cd google-maps-healthcare-scraper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Configure environment

```bash
cp .env.example .env
# Add your Google Places API key
```

### 4. Launch the GUI

```bash
python src/gui.py
```

---

## Environment Variables

```env
# .env.example
GOOGLE_PLACES_API_KEY=your_google_places_api_key_here
OUTPUT_DIR=./output
HEADLESS=false
```

---

## Requirements

```
playwright>=1.40.0
undetected-chromedriver>=3.5.0
pandas>=2.0.0
requests>=2.31.0
python-dotenv>=1.0.0
```

---

## Output Format

| Column     | Example                         |
| ---------- | ------------------------------- |
| Name       | Riverside Urgent Care           |
| Address    | 123 Main St, Columbus, OH 43215 |
| Phone      | (614) 555-0123                  |
| Email      | info@riversideurgent.com        |
| Specialty  | Urgent Care                     |
| State      | OH                              |
| Source URL | https://maps.google.com/...     |

---

## Author

**Pranay Eligeti** — [linkedin.com/in/pranay-eligeti](https://linkedin.com/in/pranay-eligeti)
