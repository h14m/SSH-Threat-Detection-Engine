import time
from parser import parse_auth_log
from alerts import generate_alerts

def main():

    print("===== REAL-TIME SSH MONITOR STARTED =====")

    while True:

        failed_attempts = parse_auth_log()

        print(failed_attempts)

        generate_alerts(failed_attempts)

        time.sleep(10)

if __name__ == "__main__":
    main()
