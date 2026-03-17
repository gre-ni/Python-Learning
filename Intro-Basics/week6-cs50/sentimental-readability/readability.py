import math


def main():
    try:
        text = input("Text: ")
    except ValueError:
        pass

    result_grade = grade(index(letters(text), sentences(text)))
    print(result_grade)


# Calculates average number of letters per 100 words in the text:
def letters(text: str):
    letters = 0
    words = text.count(" ") + 1
    for char in text:
        if char.isalnum():
            letters += 1

    return letters / words * 100


# Calculates average number of sentences per 100 words in the text
def sentences(text: str):
    words = text.count(" ") + 1
    sentences = text.count(".") + text.count("?") + text.count("!")

    return sentences / words * 100


# Coleman-Liau index:
def index(letters: float | int, sentences: float | int):
    return 0.0588 * letters - 0.296 * sentences - 15.8


def grade(index):
    index = round(index)
    if index < 1:
        return "Before Grade 1"
    elif index > 16:
        return "Grade 16+"
    else:
        return f"Grade {int(index)}"


if __name__ == "__main__":
    main()
