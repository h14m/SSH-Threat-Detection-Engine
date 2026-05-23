import re
from collections import defaultdict

LOG_FILE = "/var/log/auth.log"

def parse_auth_log():

    failed_attempts = defaultdict(int)

    patterns = [
        r"Failed password.*from (\d+\.\d+\.\d+\.\d+)",
        r"Invalid user .* from (\d+\.\d+\.\d+\.\d+)",
        r"Connection closed by authenticating user .* (\d+\.\d+\.\d+\.\d+)",
        r"Received disconnect from (\d+\.\d+\.\d+\.\d+)"
    ]

    try:
        with open(LOG_FILE, "r") as file:
            logs = file.readlines()

        for line in logs:

            for pattern in patterns:

                match = re.search(pattern, line)

                if match:

                    ip = match.group(1)

                    failed_attempts[ip] += 1

    except FileNotFoundError:
        print("[ERROR] auth.log file not found.")

    return failed_attempts
