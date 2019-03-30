import pycaptcha
from PIL import Image

img = Image.open('1.png')
a = pycaptcha.get_mode(img)
print(a)
