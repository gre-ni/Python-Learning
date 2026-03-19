import re


def main():
    email = input("What's your email? ").strip()
    
    if validate_email(email):
        print("Valid Email")
    else:
        print("Invalid Email")


def validate_email(email: str) -> bool:
    # search doesn't return bool, it returns matches, truthiness turned into boolean for return:
    return bool(re.search(r"^(\w+\.{1})?\w+@(\w+\.{1})?\w+\.(edu|com|cz|eu)$", email, re.IGNORECASE))
    

if __name__ == "__main__":
    main()