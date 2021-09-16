from PIL import Image
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(50000)

white = (255,255,255)
yellow = (255,255,0)
red = (255,0,0)

# create a polygon
def createPolygon(im,width,height) :

    i = width/8
    while i <= 3 * width/8 :
        im.putpixel((int(i), int(height/8)), red)
        i += 1
    
    i = height/8
    while i <= 3 * height/8 :
        im.putpixel((int(3 * width / 8), int(i)), red)
        i += 1

    i = 3 * width/8
    while i >= width/8 :
        im.putpixel((int(i), int(3 * height/8)), red)
        i -= 1

    i = 3 * height/8
    while i >= height/8 :
        im.putpixel((int(width / 8), int(i)), red)
        i -= 1

# boundary fill algo
def bf(im, x, y, bc, fc) :

    cc = im.getpixel((x,y))  

    if cc == bc or cc == fc :
        return 
    
    im.putpixel((x,y),fc)

    bf(im, x, y-1 , bc, fc)
    bf(im, x, y+1 , bc, fc)
    bf(im, x+1, y , bc, fc)
    bf(im, x-1, y , bc, fc)

# creating an image
im1 = Image.new(mode = "RGB",size=(400,250),color = white)
width, height = im1.size

createPolygon(im1, width, height)
bf(im1, int(width/4) , int(height/4) , red , yellow)

# show the image
# im1.show()

# show the image on graph
plt.imshow(im1)
plt.show()
