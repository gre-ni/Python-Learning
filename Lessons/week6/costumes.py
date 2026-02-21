from PIL import Image
import sys

images = []

# I will be specifying images to put into a gif through command line
for arg in sys.argv[1:]: # Skipping program name
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif",
    save_all=True,
    append_images=[images[1]],
    duration=200,
    loop=0 # Infinite
)
