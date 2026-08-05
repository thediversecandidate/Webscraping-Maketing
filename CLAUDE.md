# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

An early-stage scaffold for a marketing-focused web scraper — separate
project from `Webscraping` (the Django/Celery/Elasticsearch news-article
scraper). Currently a single demonstration script, not a working scraper
for any real target yet.

## Running

```bash
pip install -r requirements.txt
python src/webscraper.py
```

`src/webscraper.py`'s `scrape_example()` fetches the title of
`https://example.com` and writes it to `data/example.txt`; it fails soft
(returns a fallback string) rather than raising when the network is
unreachable. `data/` is created at runtime, not checked in.

## Structure

- `src/` — scraping code (currently just `webscraper.py`)
- `data/` — scraped output, created on first run
- `docs/` — currently a placeholder; intended home for scraping targets and
  data schemas per `README.md`'s "Next Steps"

There is no established convention beyond `scrape_example()`'s pattern
(fetch -> parse with BeautifulSoup -> fail soft with a fallback string) —
follow that shape when adding real scraping targets, and there is no test
suite yet to extend.
