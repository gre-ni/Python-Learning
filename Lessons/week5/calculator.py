def main():
    try:
        x = int(input("What's x? "))
    except TypeError:
        print("Wrong input, give a number.")
    print(f"x squared is {square(x)}")


def square(n):
    return n * n


if __name__ == "__main__":
    main()