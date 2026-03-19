import re

def main():
    name = input("What's your name? ").strip()
    print(reformat_name(name))


def reformat_name(name: str) -> str:
    matches = re.search(r"^(.+), ?(.+)$", name)

    if matches:
        last, first = matches.groups()
        return f"{first} {last}"


if __name__ == "__main__":
    main()