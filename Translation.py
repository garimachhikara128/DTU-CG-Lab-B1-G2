import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
plt.figure(figsize=(7,7))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-50,150)
plt.ylim(-50,150)
plt.title("Translation")

def line(x1,y1,x2,y2,c,l) :
    xl = [x1, x2]
    yl = [y1, y2]

    plt.plot(xl, yl, color=c,label = l)

def polygon(x1,y1,x2,y2,x3,y3,x4,y4,c,l) :
    xl = [x1, x2, x3, x4, x1]
    yl = [y1, y2, y3, y4, y1]

    plt.plot(xl, yl, color=c, label = l)

def circle(xc, yc, r, c, l) :
    sa = 0 * math.pi / 180
    ea = 360 * math.pi / 180

    xl = []
    yl = []

    theta = sa 
    while theta <= ea :

        x = r * math.cos(theta)
        y = r * math.sin(theta)

        xl.append(x+xc)
        yl.append(y+yc)

        theta += 0.01

    plt.scatter(xl, yl, s = 5, color = c, label = l)

def ellipse(xc, yc, rx, ry, c, l) :
    sa = 0 * math.pi / 180
    ea = 360 * math.pi / 180

    xl = []
    yl = []

    theta = sa 
    while theta <= ea :

        x = rx * math.cos(theta)
        y = ry * math.sin(theta)

        xl.append(x+xc)
        yl.append(y+yc)

        theta += 0.01

    plt.scatter(xl, yl, s = 5, color = c, label = l)

print("--------- TRANSLATION ---------")
print("1. Line")
print("2. Polygon")
print("3. Circle")
print("4. Ellipse")

choice = int(input("Enter your choice : "))

if choice == 1 :

    x1 = int(input("x1 : "))
    y1 = int(input("y1 : "))
    x2 = int(input("x2 : "))
    y2 = int(input("y2 : "))
    tx = int(input("tx : "))
    ty = int(input("ty : "))

    line(x1,y1,x2,y2,"red","Original Line")
    
    x1_ = x1 + tx 
    y1_ = y1 + ty
    x2_ = x2 + tx
    y2_ = y2 + ty

    line(x1_,y1_,x2_,y2_,"green", "Translated Line")

elif choice == 2 :

    x1 = int(input("x1 : "))
    y1 = int(input("y1 : "))
    x2 = int(input("x2 : "))
    y2 = int(input("y2 : "))
    x3 = int(input("x3 : "))
    y3 = int(input("y3 : "))
    x4 = int(input("x4 : "))
    y4 = int(input("y4 : "))
    tx = int(input("tx : "))
    ty = int(input("ty : "))

    polygon(x1,y1,x2,y2,x3,y3,x4,y4, "red", "Original Polygon")
    
    x1_ = x1 + tx 
    y1_ = y1 + ty
    x2_ = x2 + tx
    y2_ = y2 + ty
    x3_ = x3 + tx
    y3_ = y3 + ty
    x4_ = x4 + tx
    y4_ = y4 + ty

    polygon(x1_,y1_,x2_,y2_,x3_,y3_,x4_,y4_, "green", "Translated Polygon")

elif choice == 3 :

    x = int(input("x : "))
    y = int(input("y : "))
    r = int(input("r : "))
    tx = int(input("tx : "))
    ty = int(input("ty : "))

    circle(x,y,r, "red", "Original Circle")

    x_ = x + tx 
    y_ = y + ty

    circle(x_, y_, r, "green", "Translated Circle")

elif choice == 4 :

    x = int(input("x : "))
    y = int(input("y : "))
    rx = int(input("rx : "))
    ry = int(input("ry : "))
    tx = int(input("tx : "))
    ty = int(input("ty : "))

    ellipse(x,y,rx,ry, "red", "Original Ellipse")

    x_ = x + tx 
    y_ = y + ty

    ellipse(x_,y_,rx,ry, "green", "Translated Ellipse")

plt.legend()
plt.show()