
# take the input
xwmin = int(input("X W Min : "))
ywmin = int(input("Y W Min : "))
xwmax = int(input("X W Max : "))
ywmax = int(input("Y W Max : "))

x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

TOP = 8     # 1000
BOTTOM = 4  # 0100
RIGHT = 2   # 0010
LEFT = 1    # 0001

def computeCode(x,y) :

    code = 0

    if x < xwmin :
        code |= LEFT 

    if x > xwmax :
        code |= RIGHT 

    if y < ywmin :
        code |= BOTTOM 

    if y > ywmax :
        code |= TOP

    return code  

m = (y2-y1)/(x2-x1)

while True :

    # Step 1 : Find the codes for the end points
    code1 = computeCode(x1,y1)
    code2 = computeCode(x2,y2)

    # Step 2 : If both the codes are 0 => line lies inside the window
    if code1 == 0 and code2 == 0 :
        print("Line is visible from %.2f, %.2f to %.2f,%.2f" % (x1,y1,x2,y2)) 
        break 

    # Step 3a : code1 & code2 != 0 => line is outside the window
    elif (code1 & code2) != 0 :
        print("Outside the window")
        break 

    # Step 3b : clipping
    else : 

        pick = 0 
        x = 0.0
        y = 0.0

        if code1 != 0 :
            code_out = code1 
            pick = 1
        else :
            code_out = code2 
            pick = 2

        if code_out & LEFT :
            x = xwmin
            y = m * (xwmin - x1) + y1

        elif code_out & RIGHT :
            x = xwmax
            y = m * (xwmax - x1) + y1

        elif code_out & TOP :
            y = ywmax
            x = (ywmax - y1) / m + x1 

        elif code_out & BOTTOM :
            y = ywmin
            x = (ywmin - y1) / m + x1 

        if pick == 1 :
            x1 = x
            y1 = y

        elif pick == 2 :
            x2 = x
            y2 = y
