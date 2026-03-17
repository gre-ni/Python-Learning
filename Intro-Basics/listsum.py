list = [2, 3, 6, 7, 7, 1]

def sumevens(l):
    if isinstance(l, list):
        raise TypeError("Input should be a list.")
    
    sum = 0
    for item in l: 
        if (int(item) % 2 == 0): #converting in case numbers are strings
            sum = sum + 1
        
    return sum
        