# 2. Count occurrences: Implement count(s, char) that counts how many times a character appears in a string. So count("banana", "a") returns 3.

def main():
    string = input("String: ")
    char = input("Char: ")
    print(count(string,char))


def count(s,char):
    if len(s) == 0:
        return 0
    
    if s[0] == char:
        return 1 + count(s[1:], char)

    return 0 + count(s[1:], char)


if __name__ == "__main__":
    main()