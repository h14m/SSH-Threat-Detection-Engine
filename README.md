# SSH Threat Detection Engine

## Overview

Python-Based SSH Threat Detection Engine is a lightweight security monitoring tool that analyzes Linux SSH authentication logs to detect brute-force attempts, invalid username activity, and suspicious attacker IP addresses.

The tool parses `/var/log/auth.log`, extracts attacker IPs, counts failed login attempts, generates alerts, enriches IP information using GeoIP lookup, and stores investigation results in CSV reports.

This project focuses on Python-based log parsing and SSH threat detection without relying on external SIEM platforms.

---

## Features

- Linux SSH authentication log parsing
- Failed login detection
- Invalid username detection
- SSH brute-force detection
- Top attacker IP identification
- GeoIP lookup for attacker location
- CSV-based incident report generation
- Streamlit dashboard for attack statistics
- Terminal-based alert output

---

## Technologies Used

- Python
- Ubuntu Linux
- AWS EC2
- Streamlit
- Pandas
- Matplotlib
- Colorama
- Requests

---

## Project Structure

```text
SSH-Threat-Monitor/
├── main.py
├── parser.py
├── alerts.py
├── dashboard.py
├── requirements.txt
├── README.md
├── logs/
├── reports/
└── screenshots/
