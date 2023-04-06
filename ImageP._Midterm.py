
from PIL import Image
import numpy

def get_the_crypto_message(image, sentinel):
    image = Image.open(image)
    width, height = image.size
    bitplane = numpy.zeros((height, width))
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            lsb = pixel & 1
            bitplane[y, x] = lsb


    message = ""
    bitbuffer = ""
    for i in range(width -1 , -1,-1):
        for j in range(height  -1,-1, -1):
            bitbuffer += str(int(bitplane[j, i]))
            if len(bitbuffer) == 8:
                character = chr(int(bitbuffer, 2))
                if character == sentinel:
                    break
                else:
                    message = str(character) + message
                    bitbuffer = ""

    return message

print(get_the_crypto_message('68.tif', '&'))
