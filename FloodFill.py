from PIL import Image
import matplotlib.pyplot as plt

import sys
sys.setrecursionlimit(50000)

white = (255,255,255)
yellow = (255,255,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)

# create a polygon
def createPolygon(im,width,height) :

    i = width/8
    while i <= 3 * width/8 :
        im.putpixel((int(i), int(height/8)), red)
        i += 1
    
    i = height/8
    while i <= 3 * height/8 :
        im.putpixel((int(3 * width / 8), int(i)), blue)
        i += 1

    i = 3 * width/8
    while i >= width/8 :
        im.putpixel((int(i), int(3 * height/8)), green)
        i -= 1

    i = 3 * height/8
    while i >= height/8 :
        im.putpixel((int(width / 8), int(i)), black)
        i -= 1

# boundary fill algo
def ff(im, x, y, ic, fc) :

    cc = im.getpixel((x,y))  

    if cc != ic  :
        return 
    
    im.putpixel((x,y),fc)

    ff(im, x, y-1 , ic, fc)
    ff(im, x, y+1 , ic, fc)
    ff(im, x+1, y , ic, fc)
    ff(im, x-1, y , ic, fc)

# creating an image
im1 = Image.new(mode = "RGB",size=(400,250),color = white)
width, height = im1.size

createPolygon(im1, width, height)
im2 = im1.copy()
ff(im1, int(width/4) , int(height/4) , white , yellow)

# show the image
# im1.show()

# show the image on graph
# plt.imshow(im1)
# plt.show()

# subplots
f, axis = plt.subplots(1, 2, figsize= (10,5))

axis[0].imshow(im2)
axis[1].imshow(im1)

axis[0].set_title("Before Flood Fill Algo")
axis[1].set_title("After Flood Fill Algo")

plt.show()

