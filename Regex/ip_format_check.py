import re
import sys

def main():
    print(validate_ip_address(input("IPv4 Address: ")))


def validate_ip_address(input: str) -> bool:
    return bool(re.search(r"^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$", input))


if __name__ == "__main__":
    main()