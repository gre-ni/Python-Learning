# 3. Flatten a nested list: Implement flatten(lst) that takes a arbitrarily nested list and returns a flat one. So flatten([1, [2, [3, 4]], 5]) returns [1, 2, 3, 4, 5].

def main():
    l = [4, 5, [7, 8], 9]
    
    try:
        print(flatten(l))
    except ValueError:
        print("Not a valid list.")


def flatten(l):
    
    if not isinstance(l, list):
        raise ValueError("List should not be empty")
    
    if l == []:
        return []
    
    if isinstance(l[0], list):
        return flatten(l[0]) + flatten(l[1:])
    
    return [l[0]] + flatten(l[1:])



if __name__ == "__main__":
    main()