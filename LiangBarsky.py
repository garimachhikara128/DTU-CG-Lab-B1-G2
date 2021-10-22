
xwmin = int(input("X W Min : "))
ywmin = int(input("Y W Min : "))
xwmax = int(input("X W Max : "))
ywmax = int(input("Y W Max : "))

x1 = int(input("x1 : "))
y1 = int(input("y1 : "))
x2 = int(input("x2 : "))
y2 = int(input("y2 : "))

dx = x2 - x1
dy = y2 - y1

p = []
p.append(-dx)
p.append(dx)
p.append(-dy)
p.append(dy)

q = []
q.append(x1 - xwmin)
q.append(xwmax - x1)
q.append(y1 - ywmin)
q.append(ywmax-y1)

initial_time = 0 
final_time = 1

flag = True
somethingInside = True

x1_ = x1
y1_ = y1
x2_ = x2
y2_ = y2

for i in range(len(p)) :

    if p[i] == 0 :

        if q[i] < 0 :
            somethingInside = False
        else :
            somethingInside = True

        flag = False
        break

    elif p[i] < 0 :
        initial_time = max(initial_time, q[i]/p[i])
    
    elif p[i] > 0 :
        final_time = min(final_time, q[i]/p[i])

# if flag is true => none of the p[i] was 0 => you should check if initial_time < final_time
if flag :

    if initial_time < final_time :

        x1_ = x1 + initial_time * dx 
        y1_ = y1 + initial_time * dy

        x2_ = x1 + final_time * dx 
        y2_ = y1 + final_time * dy

        somethingInside = True

    else :
        somethingInside = False


if somethingInside :
    print("Line is visible from %.2f,%.2f to %.2f,%.2f" % (x1_,y1_,x2_,y2_))
else :
    print("Line is outside the window")


