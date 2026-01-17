import sys

# Countdown function:
def countdown(n):
    if n == 0: # base case
        print("Done!")
        return

    print(n)
    countdown(n - 1) # recursive case

# Factorial function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Making a sum of a list:
def sum_list(numbers):
    if not numbers: # if bool(numbers) == False:
        return 0
    return numbers[0] + sum_list(numbers[1:]) # returns first number, rest of the list called recursively
    # until all the numbers have been sliced out and list is empty
    # after hitting base case 0, the indexed number is being returned to previous function call
    # each function call adds next number from the list, resulting in sum

# Dividing by 2 until it can't:
import sys
number = int(input("Give me a number divisble by two: "))

def divide(n):
    if (n % 2) != 0:
        raise ValueError("Number must be divisible by 2")
    
    if n == 2:
        return 1 

    n = n // 2 # Returns an integer, rather than a float.
    return 1 + divide(n)

try:
    counter = divide(number)
except ValueError:
    sys.exit("Your number isn't divisible by two!")
    
print(f"I've divided your number {counter} times!")
   