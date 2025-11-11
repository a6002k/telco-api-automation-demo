# Telecom API Automation — Safe Demo (Python)

This repository contains a **safe, anonymized, and runnable demo** that illustrates how to automate
REST API interactions typical for telecom / SIM-management integrations (fetching SIM lists, parsing JSON, exporting CSV).

**Important:** This demo **does not** contain any real credentials or private endpoints. It runs offline
using built-in mock data by default, so you (or a client) can run it immediately without keys.

## Files in this repository

- `safe_demo_telco_api.py` — main demo script. Uses mock data if no `DEMO_API_URL` environment variable is set.
- `demo_output.txt` — example output from running the script (included here so viewers can see realtime output without execution).
- `.gitignore` — ignores environment files and local artifacts.
- `LICENSE` — MIT license.
- `sims_data_*.csv` — sample CSV files generated when running the script (not included to keep repo small).

## How to run (locally)

1. Install Python 3.8+.
2. Optionally, create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt  # (optional; requirements empty by default)
   ```
3. Run the script:
   ```bash
   python safe_demo_telco_api.py
   ```
This will create a CSV file with mock SIM records in the current directory.

## How to test with a public demo endpoint (optional)

If you want others to be able to run the script against a reachable demo API, set the environment variable `DEMO_API_URL`
to a URL that returns JSON. The script will try to detect lists under `elements` or top-level lists.

Example on Unix-like shells:
```bash
export DEMO_API_URL="https://demo.example.com/v2/group/123/sims"
python safe_demo_telco_api.py
```

## Notes for clients / reviewers

- The repository purpose is to **demonstrate structure and approach** (requests → JSON parsing → CSV export → filename conventions),
  not to expose private production code or credentials.
- If you want a runnable live demo that others can open directly in the browser, we can deploy the mock API to a free host
  (e.g., Render.com, Railway.app) and update `DEMO_API_URL` accordingly. I can help with that on request.

---
Generated: 2025-11-11 03:17:30Z (UTC)
