from PIL import Image

image = Image.open("1.jpg")
grey = image.convert("L")
grey.show()