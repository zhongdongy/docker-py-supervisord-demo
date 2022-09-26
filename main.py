import time
import sys


def main():
    while True:
        time.sleep(2)
        try:
            import requests
            resp = requests.get('https://www.google.com')
            sys.stdout.write(f"{resp.status_code}\n")
        except Exception as e:
            sys.stderr.write(f"Unable to request `www.google.com`: {e}\n")


if '__main__' == __name__:
    main()
