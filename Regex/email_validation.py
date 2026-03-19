import re


def main():
    email = input("What's your email? ").strip()
    
    if validate_email(email):
        print("Valid Email")
    else:
        print("Invalid Email")


def validate_email(email: str) -> bool:
    # This search doesn't return bool, it returns matches, if checks truthiness
    if re.search(r"^(\w+\.{1})?\w+@(\w+\.{1})?\w+\.(edu|com|cz|eu)$", email, re.IGNORECASE):
        return True
    else: 
        return False
    

if __name__ == "__main__":
    main()