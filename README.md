# AWS-Based SOC Monitoring & SIEM Threat Detection Platform

## Overview

This project is a Security Operations Center (SOC) Home Lab designed to simulate real-world security monitoring, threat detection, and incident investigation workflows. 

The environment consists of an AWS-hosted Ubuntu server acting as a monitored asset, Kali Linux as the attack machine, and Splunk Enterprise as the Security Information and Event Management (SIEM) platform.

The solution collects and analyzes SSH authentication logs, detects reconnaissance and unauthorized access attempts, identifies attacker IP addresses, and provides SOC-style dashboards for monitoring security events in real time.

---

## Architecture

Kali Linux (Attacker)
↓
AWS EC2 Ubuntu Server
↓
Linux Authentication Logs (auth.log)
↓
Splunk Enterprise SIEM
↓
Dashboards, Detection Rules, Investigation

---

## Key Features

### Security Monitoring

* Real-time SSH log monitoring
* Linux authentication log analysis
* Suspicious connection tracking
* Unauthorized access detection

### Threat Detection

* Invalid username detection
* SSH reconnaissance detection
* Connection anomaly detection
* Top attacker IP identification

### SIEM & Threat Hunting

* Splunk Enterprise deployment
* Custom SPL detection queries
* Security event investigation
* Log correlation and analysis

### SOC Dashboard

* Top Attacker IPs
* SSH Attack Timeline
* Top Targeted Usernames
* SSH Scanning Activity
* Recent SSH Attack Events
* Successful vs Failed Access Analysis

### Attack Simulation

* Kali Linux attack platform
* Nmap reconnaissance simulation
* SSH enumeration testing
* Attack-to-detection validation

---

## Technologies Used

* AWS EC2
* Ubuntu Linux
* Splunk Enterprise
* Kali Linux
* Python
* Linux Authentication Logs
* SPL (Search Processing Language)
* Git
* Github

---

## Project Structure

AWS-SOC-Monitoring-Platform/

├── main.py
├── parser.py
├── alerts.py
├── dashboard.py
├── requirements.txt
├── README.md
├── logs/
├── reports/
│   └── incident_report.md
└── screenshots/
---

## SOC Detection Queries
## Detection Rules

### SSH Brute Force Detection
```spl
index=* "Failed password"
| stats count by src_ip
| where count > 10
```

Purpose:
Detect repeated failed SSH authentication attempts from a single source IP.

---

### Failed Login Trend Analysis

```spl
index=* "Failed password"
| timechart count
```

Purpose:
Monitor spikes in authentication failures and identify attack patterns.

---
### Top Attacker IPs

```spl
index=* "Invalid user"
| rex "from (?<attacker_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by attacker_ip
| sort - count
```

### SSH Reconnaissance Detection

```spl
index=* "Invalid user"
| rex "from (?<attacker_ip>\d+\.\d+\.\d+\.\d+)"
| stats count by attacker_ip
| where count > 3
```
## Incident Investigation Workflow

1. Generate SSH attack activity from Kali Linux.
2. Collect Linux authentication logs from AWS EC2 Ubuntu.
3. Ingest logs into Splunk Enterprise.
4. Execute SPL detection queries.
5. Identify attacker IP addresses.
6. Analyze attack timeline and targeted usernames.
7. Investigate indicators of compromise (IOCs).
8. Document findings in incident reports.
---

## Screenshots

### SOC Monitoring Dashboard

![Dashboard](screenshots/dashboard.png)

### SSH Reconnaissance Alert

![Alert](screenshots/alerts.png)

### Top Attacker IP Analysis

![Top Attacker IPs](screenshots/top_attacker_ips.png)

---

## SOC Analyst Skills Demonstrated

* SIEM Monitoring
* Security Event Analysis
* Log Analysis
* Threat Detection
* Threat Hunting
* Incident Investigation
* Incident Response
* Detection Engineering
* Splunk Administration
* Linux Security Monitoring
* AWS Security Monitoring
* MITRE ATT&CK Mapping
* Security Event Correlation
---
## MITRE ATT&CK Mapping

The attack scenarios and detections implemented in this project align with the following MITRE ATT&CK techniques:

| Technique ID | Technique Name | Description |
|-------------|----------------|-------------|
| T1110 | Brute Force | Repeated SSH authentication attempts against user accounts |
| T1595 | Active Scanning | Reconnaissance and service discovery using Nmap |
| T1078 | Valid Accounts | Attempted use of legitimate account credentials |
| T1046 | Network Service Discovery | Identification of exposed services and ports |

This mapping helps security analysts understand attacker behavior and improves detection engineering capabilities.
---
## Relevant SOC Concepts

* SIEM
* SOC Operations
* Threat Detection
* Threat Hunting
* Incident Response
* Security Monitoring
* Event Correlation
* MITRE ATT&CK
* Linux Log Analysis
* AWS Security
* Splunk SPL
  
---

## Future Enhancements

* Windows Sysmon Integration
* Splunk Universal Forwarder Deployment
* Email Alerting
* Threat Intelligence Integration
* Automated Incident Response
* Multi-Host Log Collection

---

## Author

Mahi Honnagol
Cybersecurity | SOC Analyst | Cloud Security Enthusiast
