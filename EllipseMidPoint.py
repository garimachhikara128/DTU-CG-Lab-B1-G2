import matplotlib.pyplot as plt

rx = int(input("Radius on X : "))
ry = int(input("Radius on Y : "))
xc = int(input("Center on X : "))
yc = int(input("Center on Y : "))

# Region 1
x = 0
y = ry 

plt.style.use('seaborn')

p1 = (ry**2) + (0.25 * (rx**2)) - (ry * (rx**2))

while (x * (ry**2) < y * (rx**2)) :

    plt.scatter(x + xc , y + yc, color = 'red')
    plt.scatter(x + xc, -y + yc, color = 'red')
    plt.scatter(-x + xc , y + yc, color = 'red')
    plt.scatter(-x + xc , -y + yc, color = 'red')

    if p1 < 0 :
        x += 1
        p1 = p1 + (2 * (ry**2) * x) + (ry**2)

    else :
        x += 1
        y -= 1
        p1 = p1 + (2 * (ry**2) * x) - (2 * (rx**2) * y) + (ry**2)

# Region 2

p2 = (((x + 0.5)**2) * (ry**2)) + (((y-1)**2) * (rx**2)) - ((rx**2) * (ry**2))

while y >=0 :

    plt.scatter(x + xc , y + yc, color = 'red')
    plt.scatter(x + xc, -y + yc, color = 'red')
    plt.scatter(-x + xc , y + yc, color = 'red')
    plt.scatter(-x + xc , -y + yc, color = 'red')

    if p2 > 0 :
        y -= 1
        p2 = p2 - (2 * y * (rx**2)) + (rx**2)

    else :
        x += 1
        y -= 1
        p2 = p2 + (2 * (ry**2) * x) - (2 * y * (rx**2)) + (rx**2)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.title("Mid Point Ellipse Drawing Algo")
plt.show()