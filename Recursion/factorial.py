
n = int(input("Give me a number: "))

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(n))