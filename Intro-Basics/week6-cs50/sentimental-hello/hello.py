def main():
    name = input("What is your name? ")
    print(hello(name))


def hello(name="world"):
    return f"hello, {name}"


if __name__ == "__main__":
    main()
