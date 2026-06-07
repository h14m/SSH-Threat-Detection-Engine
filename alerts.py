import requests
import csv
import smtplib
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style, init

init(autoreset=True)

THRESHOLD = 3
REPORT_FILE = "reports/attack_report.csv"

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

alerted_ips = set()


def get_ip_location(ip):
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=2
        )

        data = response.json()

        country = data.get("country", "Unknown")
        city = data.get("city", "Unknown")

        return f"{city}, {country}"

    except Exception:
        return "Unknown Location"


def send_email_alert(ip, count, location):
    subject = f"[SSH ALERT] Brute Force Detected from {ip}"

    body = f"""
SSH Threat Detection Alert

Alert Type      : Possible SSH Brute Force Attack
Source IP       : {ip}
Failed Attempts : {count}
Location        : {location}
Timestamp       : {datetime.now()}

Recommended SOC Actions:
1. Investigate the source IP address.
2. Review /var/log/auth.log for related activity.
3. Check if the IP attempted multiple usernames.
4. Block the IP if malicious behavior is confirmed.
"""

    message = MIMEMultipart()
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(message)
        server.quit()

        print(Fore.BLUE + f"[EMAIL SENT] Alert email sent for {ip}")

    except Exception as e:
        print(Fore.RED + f"[EMAIL ERROR] {e}")


def generate_alerts(failed_attempts):
    print(Fore.CYAN + "\n===== SSH BRUTE FORCE ALERTS =====\n")

    total_attempts = sum(failed_attempts.values())

    if failed_attempts:
        top_attacker = max(failed_attempts, key=failed_attempts.get)

        print(Fore.YELLOW + f"[STATS] Total Failed Attempts: {total_attempts}")
        print(Fore.YELLOW + f"[STATS] Top Attacker IP: {top_attacker}")
        print(Fore.YELLOW + f"[STATS] Highest Attempts: {failed_attempts[top_attacker]}\n")

    else:
        print(Fore.YELLOW + "[STATS] No failed login attempts detected.\n")

    os.makedirs("reports", exist_ok=True)

    with open(REPORT_FILE, "a", newline="") as csvfile:
        fieldnames = [
            "Timestamp",
            "IP Address",
            "Location",
            "Failed Attempts",
            "Alert"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        for ip, count in failed_attempts.items():
            alert_status = "NO"
            location = get_ip_location(ip)

            print(
                Fore.GREEN +
                f"[INFO] IP: {ip} | Location: {location} | Failed Attempts: {count}"
            )

            if count >= THRESHOLD:
                alert_status = "YES"

                print(
                    Fore.RED +
                    Style.BRIGHT +
                    f"[ALERT] Possible Brute Force Attack Detected from {ip}"
                )

                if ip not in alerted_ips:
                    send_email_alert(ip, count, location)
                    alerted_ips.add(ip)

            writer.writerow({
                "Timestamp": datetime.now(),
                "IP Address": ip,
                "Location": location,
                "Failed Attempts": count,
                "Alert": alert_status
            })

    print(Fore.CYAN + "\n[INFO] CSV Report Updated Successfully\n")
