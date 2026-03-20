import re


def main():
    url = input("URL").strip().lower()
    username = extract_username_b(url)
    print(f"Username: {username}") 


def extract_username_a(url: str) -> str | None:
    return re.sub(r"^(https?://)?(www\.)?twitter\.com/","", url)


# Alternative which would return information about 
def extract_username_b(url: str) -> str | None:
    username = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)/?", url, re.IGNORECASE)
    if username:
        return username.group(1)
    else: 
        return None

if __name__ == "__main__":
    main()