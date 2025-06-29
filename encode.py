from PIL import Image
from math import ceil

with open("data.txt", "r") as f:
    data = f.read()

length = ceil(len(data) / 3)

answer = 0
while answer**2 < length:
    answer += 1

img = Image.new("RGB", (answer, answer))
pixels = img.load()
i = 0
for col in range(answer):
    for row in range(answer):
        if len(data) >= i+3:
            pixels[row,col] = (ord(data[i]), ord(data[i+1]), ord(data[i+2]))
        elif len(data) >= i+2:
            pixels[row,col] = (ord(data[i]), ord(data[i+1]), 0)
        elif len(data) >= i+1:
            pixels[row,col] = (ord(data[i]), 0, 0)
        else:
            pixels[row,col] = (0, 0, 0)
        i += 3

img.save("data.png")