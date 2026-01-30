# Testing writing a library to use in another file:
def hello(name):
        print(f"hello, {name}")
        
def goodbye(name):
        print(f"goodbye, {name}")

def main():
    print(hello("world"))
    print(goodbye("world"))
        
# Only run main when file is directly run from command line:
if __name__ == "__main__":
    main()