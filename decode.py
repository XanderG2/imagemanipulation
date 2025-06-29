from PIL import Image

chrs = []

with Image.open('data.png') as im:
    pix = im.load()
    width, height = im.size
    for row in range(height):
        for char in range(width):
            pixel = pix[char, row]
            for char in pixel:
                chrs.append(chr(char) if not char == 0 else "")

string = "".join(chrs)

with open("output.txt", "w") as f:
    f.write(string)