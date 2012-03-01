from PIL import Image
import _imaging
import glob, os

size = 81, 81

for (i, infile) in enumerate(glob.glob("fb_photos/*.jpg"), 1):
    im = Image.open(infile)
    im.save("gallery-big/big-%d.jpg" % i, "JPEG")
    im.thumbnail(size, Image.ANTIALIAS)
    im.save("gallery-thumb/thumb-%d.jpg" % i, "JPEG")
