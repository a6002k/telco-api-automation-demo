# Telecom API Automation — Safe Demo (Python)

Safe demo of Telecom API automation with Python — fetch SIM data, parse JSON, export XLSX

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

## Requirements

- Python 3.8+
- pandas
- openpyxl (for XLSX export)

Install dependencies:

```bash
pip install pandas openpyxl
```

## Get the repository

### 1️⃣ Using Git (recommended if Git is installed)
```bash
git clone https://github.com/a6002k/telco-api-automation-demo.git
cd telco-api-automation-demo
```
### 2️⃣ Download ZIP (if Git is not installed)
- Go to the repository page: https://github.com/a6002k/telco-api-automation-demo
- Click Code → Download ZIP
- Unzip the downloaded file to any folder
- Open CMD or PowerShell and navigate to the folder:
```cmd
cd path\to\unzipped\folder
```

## How to run

### 1️⃣ Using mock data (default)

```bash
python safe_demo_telco_api.py
```

### 2️⃣ Using the working demo API

Set the environment variable DEMO_API_URL to fetch real JSON from the safe demo API.

**Windows CMD:**
```bash
set DEMO_API_URL=https://mocki.io/v1/d1b5ec31-b1cb-4a7c-88ef-4307cfd17aa8
python safe_demo_telco_api.py
```

**Linux / Mac:**
```bash
export DEMO_API_URL="https://mocki.io/v1/d1b5ec31-b1cb-4a7c-88ef-4307cfd17aa8"
python safe_demo_telco_api.py
```

Script fetches JSON from the URL and exports to sims_data_*.xlsx with 3 test SIM records.
ICCID numbers stored as text to preserve all digits.
Safe demo — no private credentials used.
If the variable is not set or fetching fails, mock data will be used automatically.

---

### 👤 Author

**Alexander Kolbin**  
IT Systems Specialist with 30+ years of experience (World Bank Group).  
Recent work — Python automation for telecom API platforms.  
Developed scripts for **Pond Mobile** to automate large-scale API requests to **Telna servers** (handling data for ~100,000 SIM cards).

