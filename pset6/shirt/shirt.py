import sys
from PIL import Image, ImageOps
from os import path

l = (".png", ".jpg", ".jpeg")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    try:
        if  sys.argv[1].lower().endswith(l) and sys.argv[2].lower().endswith(l):
            r1, e1 = path.splitext(sys.argv[1])
            r2, e2 = path.splitext(sys.argv[2])
            if e1 == e2:
                muppet = Image.open(sys.argv[1])
                shirt = Image.open("shirt.png")
                photo = ImageOps.fit(muppet, shirt.size)
                photo.paste(shirt, shirt)
                photo.save(sys.argv[2])
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid input")
    except FileNotFoundError:
        sys.exit("File does not exist")
