from PIL import Image

image = Image.open("1.jpg")
trans = image.convert("LA")
trans.save("transperant.png")
trans.show()