import re
import sys


def main():
    print(parse_youtube(input("HTML: ")))


def parse_youtube(html:str):
    # It needs to check that the link is even youtube
    # Extract only the code
    # Do I have to check the HTML formatting, too?
    if match := re.search("^<.*src=\"()\"", html):
        video_code = match.group(1)
        
        
    else:
        return None


if __name__ == "__main__":
    main()