"""
safe_demo_telco_api.py

Safe, anonymized demo script illustrating fetching SIM data (mock or demo API),
parsing JSON, and exporting to XLSX with ICCID stored as text to preserve full digits.

Requirements: pandas

Example:
    python safe_demo_telco_api.py
"""

import os
import pandas as pd
from datetime import datetime

DEMO_API_URL = os.environ.get("DEMO_API_URL", "").strip()

def get_mock_sims():
    return [
        {"iccid": "8901000123456789012", "status": "active", "plan": "Data 10GB", "last_seen": "2025-10-30T12:01:00Z"},
        {"iccid": "8901000987654321098", "status": "inactive", "plan": "Voice Only", "last_seen": "2025-09-11T09:15:00Z"},
        {"iccid": "8901000555555555555", "status": "suspended", "plan": "IoT - Basic", "last_seen": "2025-11-01T06:21:00Z"}
    ]

def fetch_sims_from_remote(url):
    try:
        import requests
    except Exception:
        print("requests library not available; using mock data.")
        return get_mock_sims()
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, dict) and "elements" in data:
            return data["elements"]
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            for v in data.values():
                if isinstance(v, list):
                    return v
        return get_mock_sims()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}; using mock data.")
        return get_mock_sims()

def save_to_xlsx(sims, filename="sims_data.xlsx"):
    df = pd.DataFrame(sims)
    if "iccid" in df.columns:
        df["iccid"] = df["iccid"].astype(str)
    df.to_excel(filename, index=False)

def main():
    if DEMO_API_URL:
        print("DEMO_API_URL set. Attempting remote fetch...")
        sims = fetch_sims_from_remote(DEMO_API_URL)
    else:
        print("No DEMO_API_URL; using mock data.")
        sims = get_mock_sims()

    save_name = f"sims_data_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.xlsx"
    save_to_xlsx(sims, save_name)
    print(f"Saved {len(sims)} record(s) to {save_name}")

if __name__ == '__main__':
    main()
