# 1. Power: Implement power(base, exp) that raises a number to an exponent. So power(2, 4) returns 16. No using **.

def main():
    base = int(input("Number: "))
    exp = int(input("Exponent: "))
    
    print(power(base,exp))

def power (base, exp):
    
    if exp == 0:
        return 1
    
    if exp == 1:
        return base
    
    return power(base, exp - 1) * base

if __name__ == "__main__":
    main()