def enigmatic(x):  
    return [int(str(abs(i))[::-1]) for i in x if i % 2 != 0]  

input_data = [-17, 38, -4, 9, 12, -3]  
print(enigmatic(input_data))


def comp(data):  
    return {k: sum(v for v in vals if v % 2 == 0) for k, vals in data.items() if len(vals) > 1}  

example = {"A": [3, 8, 2], "B": [1, 7], "C": [4, 0, 5, 9]}  
print(comp(example))  
