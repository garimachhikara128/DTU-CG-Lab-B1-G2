import matplotlib.pyplot as plt
import math

# take input
sa = int(input("Start Angle ? "))
ea = int(input("End Angle ? "))
rx = int(input("X Radius ? "))
ry = int(input("Y Radius ? "))
xc = int(input("X Center ? "))
yc = int(input("Y Center ? "))

# convert degree to radians
sa = sa * math.pi / 180
ea = ea * math.pi / 180

plt.style.use('seaborn')
plt.figure(figsize=(7,7))
plt.scatter(xc , yc , color = 'green')

theta = sa 

while theta <= ea :

    x = rx * math.cos(theta)
    y = ry * math.sin(theta)

    plt.scatter(x + xc , y + yc , color = 'red')

    theta += 0.01

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.title("Circular Arc Drawing Algo")
plt.show()