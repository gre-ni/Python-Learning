import sys

# Handling  Index errors: 
if len(sys.argv) < 2:
    sys.exit("Too few arguments given.")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")

# Using command line argument for input
print(f"Hello, my name is {sys.argv[1]}.")