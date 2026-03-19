import re


def main():
    email = input("What's your email? ").strip().lower()
    
    if validate_email(email):
        print("Valid Email")
    else:
        print("Invalid Email")


def validate_email(email: str) -> bool:
    if re.search(r"^\w{1,}\.{0,1}\w{1,}@\w{2,}(\.edu|\.com|\.cz|\.eu)$", email):
        return True
    else: 
        return False
    

if __name__ == "__main__":
    main()