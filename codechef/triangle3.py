#program of given three angle giver by user and check the possibility of triangle as well as the type of triangle
#Three any angle given by user
a=int(input(""))
b=int(input(""))
c=int(input(""))
#check the possibility of the triangle by sum of all angles
angle=a+b+c
if angle==180:
    if a==90:
        print("right angled triangle")
    elif b==90:
        print("right angled triangle")
    elif c==90:
        print("right angled triangle")
    elif a>90:
        print("obtuse")
    elif b>90:
        print("obtuse")
    elif c>90:
        print("obtuse")
    else:
        print("acute")
else:
    print("triangle not possible by your given input angle")