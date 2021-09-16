import matplotlib.pyplot as plt
import math

# take input
sa = int(input("Start Angle ? "))
ea = int(input("End Angle ? "))
r = int(input("Radius ? "))
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

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    plt.scatter(x + xc , y + yc , color = 'red')

    theta += 0.01

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(-100,100)
plt.ylim(-100,100)
plt.title("Circular Arc Drawing Algo")
plt.show()