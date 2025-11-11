# Telecom API Automation — Safe Demo (Python)

This repository contains a **safe, anonymized, and runnable demo** that illustrates how to automate
REST API interactions typical for telecom / SIM-management integrations (fetching SIM lists, parsing JSON, exporting XLSX).

**Important:** This demo **does not** contain any real credentials or private endpoints. It runs offline
using built-in mock data by default.

## Files in this repository

- `safe_demo_telco_api.py` — main demo script. Uses mock data if no `DEMO_API_URL` environment variable is set.
- `demo_output.txt` — example output from running the script.
- `.gitignore` — ignores environment files and local artifacts.
- `LICENSE` — MIT license.
- `sims_data_*.xlsx` — sample XLSX files generated when running the script.

## How to run (locally)

1. Install Python 3.8+ and pandas:
   ```bash
   pip install pandas
