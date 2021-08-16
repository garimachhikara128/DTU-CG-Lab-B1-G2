import matplotlib.pyplot as plt

r = int(input("r : "))
xcenter = int(input("x : "))
ycenter = int(input("y : "))

x = 0
y = r

p = 1 - r

xc = []
yc = []

while x <= y :

    xc.append(x + xcenter)
    yc.append(y + ycenter)

    xc.append(y + xcenter)
    yc.append(x + ycenter)

    xc.append(y + xcenter)
    yc.append(-x + ycenter)

    xc.append(x + xcenter)
    yc.append(-y + ycenter)

    xc.append(-x + xcenter)
    yc.append(y + ycenter)

    xc.append(-y + xcenter)
    yc.append(x + ycenter)

    xc.append(-y + xcenter)
    yc.append(-x + ycenter)

    xc.append(-x + xcenter)
    yc.append(-y + ycenter)

    if(p < 0) :
        p = p + 2 * x + 3
    else :
        p = p + 2 * x - 2 * y + 5
        y -= 1

    x += 1 

plt.scatter(xc, yc)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-20,20)
plt.ylim(-20,20)
plt.title("Mid Point Circle Drawing Algorithm")
plt.show()