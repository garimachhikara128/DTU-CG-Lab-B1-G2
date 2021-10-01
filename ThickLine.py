import matplotlib.pyplot as plt
import math

plt.style.use('seaborn')
plt.figure(figsize=(7,5))
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(0,200)
plt.ylim(0,200)
plt.title("Thick Line Drawing Algo")

def bresehman(x1,y1,x2,y2) :
    x = x1 
    y = y1

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    p = 2 * dy - dx 

    while x <= x2 :

        plt.scatter(x, y, color = 'red')

        if(p < 0) :
            p = p + 2 * dy 
        else :
            p = p + 2 * dy - 2 * dx 
            y += 1

        x += 1 

x1 = int(input("x1 :"))
y1 = int(input("y1 :"))
x2 = int(input("x2 :"))
y2 = int(input("y2 :"))
w = int(input("thickness :"))

wy = ((w-1) * (math.sqrt( ((y2-y1)**2) + ((x2-x1)**2)) )) / (2 * abs(x2-x1))

i = 0 
while i <= wy :

    bresehman(x1,y1-i,x2,y2-i)
    bresehman(x1,y1+i,x2,y2+i)

    i += 1

plt.show()