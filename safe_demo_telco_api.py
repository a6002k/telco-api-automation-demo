#!/usr/bin/env python3
"""
safe_demo_telco_api.py

A professional demo script illustrating:
- Securely reading configuration (API URL) from a .env file
- Fallback to local mock data if .env is not found
- Fetching a list of SIM cards (demo API)
- Optional data enrichment (status per SIM)
- Exporting to XLSX with correct ICCID formatting (as text)

Requirements: pandas, openpyxl, requests, python-dotenv
"""

import os
import requests
import pandas as pd
from datetime import datetime, UTC
from dotenv import load_dotenv
from openpyxl.utils import get_column_letter

# --- Load environment variables ---
load_dotenv()

# Read URLs from .env. They will be None if not found.
API_URL = os.getenv("DEMO_API_URL")
STATUS_URL_TPL = os.getenv("SIM_STATUS_URL_TEMPLATE")

# --- Built-in mock data (fallback if .env is not found) ---
LOCAL_MOCK_DATA = {
    "elements": [
        {"iccid": "8901000123456789012", "status": "active", "plan": "Data 10GB"},
        {"iccid": "8901000987654321098", "status": "inactive", "plan": "Voice Only"},
        {"iccid": "8901000555555555555", "status": "suspended", "plan": "IoT - Basic"}
    ]
}

def fetch_remote_data(api_url: str):
    """
    Fetches data from the remote API.
    Returns a list of SIM dictionaries.
    """
    print(f"Fetching data from remote API: {api_url}...")
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status() # Will raise an error for 4xx or 5xx status
        data = response.json()
        sims = data.get("elements", [])
        print(f"Successfully fetched {len(sims)} SIM records from API.")
        return sims
    except requests.RequestException as e:
        print(f"Error during API request: {e}")
        return []

def get_local_mock_data():
    """
    Returns the built-in mock data.
    """
    print("DEMO_API_URL not found in .env. Using built-in mock data.")
    return LOCAL_MOCK_DATA.get("elements", [])

def fetch_sim_status_remote(sim, status_url_template):
    """
    (Optional) Fetches status for ONE SIM if
    status_url_template is provided.
    """
    # {iccid} in the URL will be replaced with the actual iccid
    url = status_url_template.replace("{iccid}", sim["iccid"])
    try:
        print(f"  -> Enriching data for SIM {sim['iccid']}...")
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        status_data = response.json()
        # Update the status in our dictionary
        sim["status"] = status_data.get("status", sim.get("status", "unknown"))
    except requests.RequestException as e:
        print(f"    (Failed to fetch status for {sim['iccid']}: {e})")
    return sim

def enrich_sims_with_status(sims, status_url_template):
    """
    Runs the list of SIMs through the data enrichment function.
    """
    print(f"Starting optional enrichment step...")
    enriched = []
    for sim in sims:
        enriched.append(fetch_sim_status_remote(sim, status_url_template))
    return enriched

def save_to_excel(sims):
    """
    Saves the data to an XLSX file with a timestamp.
    (This version is corrected to auto-fit columns)
    """
    if not sims:
        print("No data to save. Excel file not created.")
        return

    # Ensure iccid is saved as text
    df = pd.DataFrame(sims)
    df['iccid'] = df['iccid'].astype(str)
    
    save_name = f"sims_data_{datetime.now(UTC).strftime('%Y%m%dT%H%M%SZ')}.xlsx"
    
    # Use ExcelWriter to set column widths
    with pd.ExcelWriter(save_name, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name="SIMs")
        
        # --- ИСПРАВЛЕННЫЙ БЛОК ---
        # Auto-fit columns for readability
        worksheet = writer.sheets['SIMs']
        for col_idx, column in enumerate(df.columns):
            # Find the max length in the column
            column_length = max(df[column].astype(str).map(len).max(), len(column)) + 2
            # Convert the 0-based index to a 1-based letter (e.g., 0 -> 'A')
            col_letter = get_column_letter(col_idx + 1)
            # Set the width using the column letter
            worksheet.column_dimensions[col_letter].width = column_length
        # --- КОНЕЦ ИСПРАВЛЕНИЯ ---

    print(f"Successfully saved {len(sims)} records to file: {save_name}")
    return save_name

def main():
    """
    Main execution function.
    """
    sims = []
    if API_URL:
        # If URL is in .env - fetch from the web
        sims = fetch_remote_data(API_URL)
    else:
        # If no URL - use local data
        sims = get_local_mock_data()

    if not sims:
        print("Could not retrieve any SIMs. Exiting.")
        return

    # (Optional) If a status URL template is in .env - run enrichment
    if STATUS_URL_TPL:
        sims = enrich_sims_with_status(sims, STATUS_URL_TPL)
    else:
        print("SIM_STATUS_URL_TEMPLATE not set in .env. Skipping enrichment step.")

    # Save to Excel
    save_to_excel(sims)

if __name__ == "__main__":
    main()
