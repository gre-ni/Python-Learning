venecky = [1, 2, 4, 1, 6, 0, 1]

# I want to display number 4 (third element)
print(venecky[2])

# I want to display 0 (second element from the end)
print(venecky[-2])

# Slicing -> first index : to but not through index 
print(venecky[0:5])
# If I want to start fom the first, or go all the way to last - I can just leave that empty [:5] or [2:]

# This is also a way to write last three elements, this is useful when I have a really large list:
print(venecky[-3:])


list_length = len(venecky)
print(list_length)

list_sum = sum(venecky)
print(list_sum)

list_min = min(venecky)
print(list_min)

list_max = max(venecky)
print(list_max)

list_sorted = sorted(venecky)
print(list_sorted)

list_sorted_backwards = sorted(venecky, reverse=True)
print(list_sorted_backwards)