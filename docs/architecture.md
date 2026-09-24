# Architecture

This repository is a sanitized public portfolio implementation of a healthcare listing acquisition pattern.

## Flow

~~~text
Permitted HTML page / local fixture
              |
              v
        Playwright browser
              |
              v
        Listing card parser
              |
              v
        Record normalization
              |
              +------> optional provider page
              |                 |
              |                 v
              |          public email extraction
              |                 |
              +-----------------+
                        |
                        v
                    CSV export
~~~

## Engineering decisions

- The public demo uses a synthetic HTML fixture for deterministic tests.
- Browser automation uses standard Playwright; no anti-bot evasion or credential bypass is included.
- Provider contact extraction is best-effort; one failed provider page does not terminate the batch.
- Secrets are supplied through environment variables and excluded from Git.
- No PHI, private employer data, or real client records belong in this repository.
