from PIL import Image

image = Image.open("1.jpg")
bw = image.convert("1")
bw.show()