import qrcode

image = qrcode.make("https://uk.pinterest.com/")
image.save("qr.png", "PNG")