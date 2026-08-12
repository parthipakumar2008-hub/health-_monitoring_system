# Health Monitoring System (HMS)

A console-based Python application for collecting and monitoring village-level health information. The system records hospital details, checks water quality, registers villages and patients, tracks diseases, and displays a summary dashboard — all through simple terminal input.

## Features

- **Hospital Details** — Capture hospital name, location, and phone number (with input validation).
- **Village Management** — Choose the number of villages to record data for.
- **Water Quality Check** — Enter a pH value per village; automatically flags water as safe (6.5–8.5 pH) or unsafe.
- **Patient Registration** — Register the number of people per village and collect each patient's name and age.
- **Disease Tracking** — Record whether a patient has a disease, and log the disease name if so.
- **Dashboard Summary** — Displays a consolidated report: date, total villages, water quality results, population counts, and disease records.
- **Loading Animation** — Simple progress indicator before the dashboard is shown.

## Technologies

- Python 3
- Object-Oriented Programming (classes: `Hospital`, `Villages`, `Dashboard`)

## Requirements

- Python 3.x (no external libraries needed — only built-in `time` and `datetime` modules)

## Installation

```bash
git clone https://github.com/parthipakumar2008-hub/health-_monitoring_system.git
cd health-_monitoring_system
```

## How to Run

```bash
python HMS.py
```

You'll be prompted step by step to enter:
1. Hospital name, location, and phone number
2. Number of villages
3. For each village: water pH value, number of people, and per-person name/age/disease details

At the end, a **Dashboard** summarizing all collected data is printed.

## Sample Flow

```
ENTER THE HOSPITAL NAME: City Hospital
ENTER THE HOSPITAL LOCATION: Trichy
ENTER THE HOSPITAl PHONE NUMBER: 9876543210

WHICH VILLAGE ARE YOU CHOOSING: 2

========= 1 VILLAGE =========
ENTER THE WATER QUALITY: 7.2
REGISTER IN NUMBER OF PEOPLE: 2
...

LOADING...
==========
COMPLETED 100%

================ DASHBOARD ================
DATE: 2026-08-13
TOTAL VILLAGE IS = 2
WATER RESULT= WATER IS SAFE IN VILLAGE 1
...
```

## Project Structure

```
health-_monitoring_system/
├── HMS.py        # Main application (Hospital, Villages, Dashboard classes)
└── README.md
```

## Known Limitations / Possible Improvements

- No data persistence (all data is lost when the program exits) — could add file/database storage.
- No error handling for invalid pH ranges outside expected bounds.
- Fully input-driven (console prompts) — could be extended with a GUI or web interface.
- Global-like reliance on `Villages` class attributes shared via inheritance in `Dashboard`.

## Author

**Parthipakumar**
