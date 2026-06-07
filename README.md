# SSH Threat Detection Engine

## Overview

SSH Threat Detection Engine is a Python-based security monitoring solution designed to detect and investigate SSH-related attacks on Linux systems. The tool continuously monitors Linux authentication logs, identifies brute-force attacks, invalid username attempts, and suspicious login activity, enriches attacker information using GeoIP lookup, generates automated email alerts, and stores investigation results in CSV reports.

The project demonstrates core SOC concepts including log analysis, threat detection, alert generation, incident reporting, and attacker profiling without relying on external SIEM platforms.

---

## Features

### Threat Detection

* Linux SSH authentication log monitoring
* Failed login detection
* Invalid username detection
* SSH brute-force attack detection
* Suspicious attacker IP identification
* Real-time security event monitoring

### Threat Intelligence & Enrichment

* GeoIP-based attacker location lookup
* Attacker profiling and source tracking
* Top attacker IP analysis

### Alerting & Reporting

* Automated email alert generation
* Terminal-based security alerts
* Alert deduplication to reduce notification fatigue
* CSV-based incident reporting
* Historical attack tracking

### Security Monitoring Dashboard

* Streamlit-based monitoring dashboard
* Failed login statistics
* Top attacker IP visualization
* Attack trend analysis
* Security event summaries

---

## Technologies Used

* Python
* Ubuntu Linux
* AWS EC2
* Streamlit
* Pandas
* Matplotlib
* Colorama
* Requests
* SMTP (Email Alerting)

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
│   └── attack_report.csv
├── screenshots/
│   ├── dashboard.png
│   ├── alerts.png
│   ├── top_attacker_ips.png
│   └── email_alert_notification.png
└── __pycache__/
```

## Key Security Capabilities

* Continuous SSH authentication log monitoring
* Detection of brute-force and username enumeration attempts
* GeoIP enrichment for attacker investigation
* Automated email notifications for detected threats
* CSV-based incident documentation
* Interactive dashboard for security monitoring
* AWS-hosted deployment and monitoring

## Future Improvements

* Multi-server monitoring support
* Centralized log aggregation
* Threat intelligence feed integration
* Automated IP blocking using UFW
* Slack and Microsoft Teams alert integration
* SIEM integration with Splunk or Microsoft Sentinel

## Author
Mahi Honnagol
