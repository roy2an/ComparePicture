#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
from PIL import Image, ImageDraw
from scipy.interpolate import interp1d
from pylab import *
im1, im2 = Image.open(sys.argv[1]), Image.open(sys.argv[2])
width, height = im1.size
diff = [(x, y) for x in xrange(width) for y in xrange(height) if im1.getpixel((x, y)) != im2.getpixel((x, y))]

draw = ImageDraw.Draw(im1)

for p in diff:
    draw.point(p, fill=(255,0,0))

im1.show()