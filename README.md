# Telco API Automation Demo

**Project Status:** 🚀 Demonstration (Ready for review)

This repository demonstrates skills in automating API requests for the telecommunications industry. The code here is a **demonstration of capability**, based on real commercial experience.

---

### Business Case

In the telecom industry (especially MVNO/IoT), there is a constant need to automate a wide range of tasks:

* Activating/deactivating SIM cards
* Checking a SIM's balance and status
* Topping up data or credit
* Pulling data usage statistics (CDRs)
* Bulk-updating information for thousands of devices

This demo project shows **how I approach solving these problems** using Python. It **specifically demonstrates** the core task of:
1.  Securely handling API credentials.
2.  Fetching data from an API endpoint.
3.  Exporting that data into a business-friendly Excel report.

This same logic can be expanded to automate any of the other tasks listed above.

---

### 🛠️ Tech Stack

* **Python**
* **Requests:** For making HTTP requests
* **Pandas:** For data manipulation and Excel exporting
* **Openpyxl:** The engine for writing `.xlsx` files
* **Python-dotenv:** For securely managing configuration (API URLs, keys)

---

### 🚀 How to Run This Demo

#### Step 1: Get the Code

You have two options.

**Option A: Download ZIP (Easiest, no Git needed)**
1.  On this GitHub page, click the green **`< > Code`** button.
2.  Select **`Download ZIP`**.
3.  Unzip the file to a folder on your computer.

**Option B: Git Clone (For developers)**
```bash
git clone [https://github.com/a6002k/telco-api-automation-demo.git](https://github.com/a6002k/telco-api-automation-demo.git)
cd telco-api-automation-demo
```

#### Step 2: Install Dependencies

(It is highly recommended to create a virtual environment first: `python -m venv venv`)

You must install the required libraries listed in `requirements.txt`.
```bash
pip install -r requirements.txt
```

#### Step 3: Create your `.env` file

This script reads your private API URL from a `.env` file. A template (`example.env`) is provided. You just need to copy it.

*In your Windows Command Prompt:*
```bash
copy example.env .env
```
*On Linux / Mac:*
```bash
cp example.env .env
```
*(Now you can edit the `.env` file with your real URL if needed. The demo URL from `mocki.io` should already be inside.)*

#### Step 4: Run the Script
```bash
python safe_demo_telco_api.py
```
---

### ⚙️ How It Works

* **If `DEMO_API_URL` is found in `.env`:** The script will attempt to fetch live data from that URL.
* **If `DEMO_API_URL` is not found:** The script will run in **"safe mode"** using built-in mock data (you won't see any network requests).
* **Result:** An `.xlsx` file (e.g., `sims_data_20251111T161700Z.xlsx`) will be created in the folder.

---

### ⭐ Hire Me

I am available for freelance projects (fixed-price, hourly) in API automation, integration, and Python backend development.

* **Upwork Profile:** [YOUR UPWORK PROFILE LINK HERE]
* **Email:** [YOUR EMAIL HERE]
