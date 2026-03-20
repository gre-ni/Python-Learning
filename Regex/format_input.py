import re

def main():
    name = input("What's your name? ").strip()
    print(reformat_name(name))


def reformat_name(name: str) -> str | None:
    # The walrus := operator is for when I want to simultaneously check the bool and assign value
    if matches := re.search(r"^(.+), *(.+)$", name):
        return f"{matches.group(2)} {matches.group(1)}"


if __name__ == "__main__":
    main()