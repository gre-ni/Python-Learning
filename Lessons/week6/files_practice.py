MAX_NAMES = 3

n = 0
while n < MAX_NAMES:
    name = input("What's your name? ")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n") # This causes one extra newline at the end
        
    n += 1

with open("names.txt", "r") as file:
    for line in file: # Shorthand instead of first storing lines in a list
        print("hello", line.rstrip())