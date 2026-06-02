# SSH Brute Force Investigation Report

## Incident Summary

A series of failed SSH authentication attempts were detected on the AWS EC2 Ubuntu server during routine security monitoring.

The activity indicated possible SSH brute-force and reconnaissance attempts originating from an external IP address.

---

## Detection Source

SIEM Platform: Splunk Enterprise

Log Source:

/var/log/auth.log

Detection Method:

Failed SSH authentication monitoring

---

## Indicators of Compromise (IOCs)

### Source IP

<Attacker IP>

### Target Service

SSH (Port 22)

### Indicators Observed

- Multiple failed login attempts
- Invalid username enumeration
- Repeated authentication failures
- SSH reconnaissance behavior

---

## Investigation Process

1. Reviewed Linux authentication logs.
2. Identified repeated failed login attempts.
3. Extracted attacker IP address.
4. Correlated events using Splunk SPL queries.
5. Visualized attack activity through dashboards.
6. Verified that no successful compromise occurred.

---

## Impact Assessment

No successful authentication was observed.

No unauthorized access was identified.

System integrity remained intact.

---

## Mitigation Actions

- Monitored suspicious source IP.
- Recommended IP blocking through firewall rules.
- Recommended SSH key authentication.
- Recommended disabling password-based SSH authentication.

---

## Lessons Learned

- Continuous log monitoring helps identify attacks early.
- SIEM dashboards improve visibility into suspicious activity.
- Detection rules reduce investigation time.

---

## Skills Demonstrated

- SIEM Monitoring
- Threat Detection
- Incident Investigation
- Log Analysis
- Splunk SPL
- Linux Security Monitoring
- SOC Operations
