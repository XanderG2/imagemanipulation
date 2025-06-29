from PIL import Image
from random import randint

with Image.open('img/canyon.jpg') as im:
    pix = im.load()
    width, height = im.size
    gstart = randint(0,(height//4)*3)
    bstart = randint(gstart, height)
    for row in range(height):
        color = 0
        if row >= gstart:
            color = 1
        if row >= bstart:
            color = 2
        for char in range(width):
            pixel = pix[char, row]
            oldpixel = [a for a in pixel]
            oldpixel.sort()
            newpixel = [0,0,0]
            newpixel[color] = oldpixel[0]
            pix[char, row] = tuple(newpixel)
    im.save('img/canyon2.jpg')