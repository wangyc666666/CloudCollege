#/usr/bin/python

from PIL import Image
import glob, os
#infile='20180105182239timg (1).jpg'
for infile in glob.glob("*.jpeg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile).convert("RGB")
    im.save(file + ".webp", "WEBP")
