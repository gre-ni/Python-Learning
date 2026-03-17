def main():
    while True:
        try: 
            height = int(input("Height: "))
            if height in range(1, 9):
                break
        except ValueError:
            pass

    build_pyramid(height)

def build_pyramid(height: int):
    gaps = height - 1
    
    for i in range(height):
        print(" " * (gaps), end="")
        print(("#" * (i + 1)) + "  " + ("#" * (i + 1)), end="")
        print(" " * (gaps))
        gaps -= 1

if __name__ == "__main__":
    main()