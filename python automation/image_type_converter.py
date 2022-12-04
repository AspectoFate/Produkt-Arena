from PIL import Image

import glob

print(glob.glob("*.JPG"))

for file in glob.glob("*.JPG"):
    im = Image.open(file)
    rgb_im = im.convert("RGBA")
    rgb_im.save(file.replace("jpg","png"),quality=50)

