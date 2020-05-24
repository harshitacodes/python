# a=int(input("enter the side length"))
# b=int(input("enter the side length"))
# c=int(input("enter the side length"))
# angle = a + b + c
# if angle == 180:
# 	print("possible")
# else:
# 	print("not possible")	

a = int(input("enter the length of side"))
b = int(input("enter the length of side"))
c = int(input("enter the length of side"))
if a == b and  b == c and c == a:
	print("equilateral")
elif a == c or  b == c or a == b:
	print("isosceles")
else:	
	print("scalar")	