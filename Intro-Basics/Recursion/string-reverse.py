import sys

def main():
    try: 
        reversed = string_reverse(input("String: "))
        print(reversed)
        
    except ValueError:
        sys.exit("Provide a valid string.")
    
def string_reverse(input: str) -> str:
    
    output = ""
    
    if not isinstance(input, str) or None:
        raise ValueError
    
    for letter in input:
        output = letter + output
    
    return output

def string_reverse_recursive(input: str) -> str:
    
    if len(input) == 0: # Not 1 because this also handles empty string as input
        return input
    
    return string_reverse_recursive(input[1:]) + input[0]

if __name__ == "__main__":
    main()