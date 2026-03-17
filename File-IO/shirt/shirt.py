import csv
import sys
from PIL import Image, ImageOps

def main():
    supported_formats = [".jpg", ".jpeg", ".png"]

    # Check number of CL arguments:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check valid format for both input and output:
    for format in supported_formats:
        if format in sys.argv[1]:
            if format in sys.argv[2]:
                break
            else:
                sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")

    size = (600,600) # Size of shirt image

    with Image.open(sys.argv[1]) as im:
        with Image.open("shirt.png") as shirt:
            im = ImageOps.fit(im, size)
            im.paste(shirt, shirt)
            im.save(sys.argv[2])


if __name__ == "__main__":
    main()
