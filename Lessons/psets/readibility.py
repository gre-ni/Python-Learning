def main():
    try:
        text = input("Text: ")
    except ValueError:
        pass
    
    grade = grade(index(letters(text), sentences(text)))
    print("Grade: {grade}")


# Calculates average number of letters per 100 words in the text:
def letters(text: str):
    words = 0 # Number of spaces (+ 1). I would count that every word has a space in front of it other than the first one. 
    # Do I perhaps remove numeric and special characters? Only special characters other than punctuation? Trim leading spaces to have accurate results.
    
    letters = 0 # Number of specifically letter Characters.
    # Potentially I can divide the string, separating number of spaces and number of the rest. 
    
    return letters / words * 100


# Calculates average number of sentences per 100 words in the text    
def sentences(text: str):
    # Counting "." "!" "?" characters.
    pass


# Coleman-Liau index:
def index(letters: float | int, sentences: float | int):
    return 0.0588 * letters - 0.296 * sentences - 15.8


def grade(index):
    pass
    # This will take index number and converts to string, handling edge cases


if __name__ == "__main__":
    main()