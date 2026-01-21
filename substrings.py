def count_substring(s: str, sub: str) -> int:
    if not isinstance(s, str) or not isinstance(sub, str):
        raise TypeError("Input needs to be a string.")    
    if not s: 
        raise ValueError("Needs to be a string")
    if not sub:
        raise ValueError("Needs to be a string")
    
    sub_length = len(sub)
    str_length = len(s)
    
    if sub_length > str_length:
        raise ValueError("Substring needs to be smaller or equal to string.")

    counter = 0
    
    for i in range(str_length - sub_length + 1):
        if s[i:i+sub_length] == sub:
            counter += 1
    
    return counter

string = input("Provide a string: ")
substring = input("Provide a substring: ")

try: 
    counter = count_substring(string, substring)
    print(f"{substring} is in {string} {counter} times")
    
except ValueError:
    print("Your input was invalid.")