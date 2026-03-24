from validator_collection import validators, errors

def main():
    email = input("What's your email address? ")

    try:
        print("Valid" if validators.email(email) else "Invalid")

    except (errors.InvalidEmailError, ValueError, errors.EmptyValueError, errors.CannotCoerceError):
        print("Invalid")


if __name__ == "__main__":
    main()