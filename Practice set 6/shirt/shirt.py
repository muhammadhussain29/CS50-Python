import sys
from PIL import ImageOps
from PIL import Image
from PIL.Image import Resampling

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    try:
        file1 = sys.argv[1].rsplit(".", 1)[-1].lower()
        file2 = sys.argv[2].rsplit(".", 1)[-1].lower()
        
        if file1 != file2:
            sys.exit("Input and output have different extensions")
        
        if file1 not in ["jpeg", "jpg", "png"]:
            raise IndexError

    except (FileNotFoundError, IndexError):
        sys.exit("Invalid input")

try:
    dummy = Image.open(sys.argv[1])

    shirt = Image.open("shirt.png")
    size = shirt.size

    dummy = ImageOps.fit(dummy, size, method=Resampling.BICUBIC)

    dummy.paste(shirt, shirt)

    dummy.show()
    dummy.save(sys.argv[2])

except FileNotFoundError:
    sys.exit("Input does not exist")
