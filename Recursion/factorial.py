
n = int(input("Give me a number: "))

def factorial(n):
    if not isinstance(n, (int, float)):
        raise TypeError
    
    if n < 1:
        raise ValueError
    
    n = int(n)
    
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(n))