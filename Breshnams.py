import matplotlib.pyplot as plt

x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

x = x1 
y = y1

dx = abs(x2 - x1)
dy = abs(y2 - y1)

p = 2 * dy - dx 

xc = []
yc = []

while x <= x2 :

    xc.append(x)
    yc.append(y)

    if(p < 0) :
        p = p + 2 * dy 
    else :
        p = p + 2 * dy - 2 * dx 
        y += 1

    x += 1 


plt.plot(xc, yc)  
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.xlim(0,40)
plt.ylim(0,40)
plt.title("Breshnams Algorithm")
plt.show()


