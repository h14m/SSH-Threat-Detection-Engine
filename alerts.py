import requests
import csv
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

THRESHOLD = 3
REPORT_FILE = "reports/attack_report.csv"


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

    except Exception as e:
        return "Unknown Location"


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

    # WRITE CSV REPORT
    with open(REPORT_FILE, "a", newline="") as csvfile:

        fieldnames = ["Timestamp", "IP Address", "Failed Attempts", "Alert"]

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
                    f"[ALERT] Possible Brute Force Attack Detected from {ip}\n"
                )

            writer.writerow({
                "Timestamp": datetime.now(),
                "IP Address": ip,
                "Failed Attempts": count,
                "Alert": alert_status
            })

    print(Fore.CYAN + "\n[INFO] CSV Report Updated Successfully\n")
