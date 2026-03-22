import re
import sys


def main():
    print(parse_youtube(input("HTML: ")))


def parse_youtube(html:str) -> str | None:
    if match := re.search(r"^<.*src=\"(?:(?:https?://www\.)youtube\.com/embed/(\w+))\"", html):
        video_code = match.group(1)
        return f"https://youtu.be/{video_code}"        
    else:
        return None


if __name__ == "__main__":
    main()