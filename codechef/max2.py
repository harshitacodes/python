# a = int(input("enter the number"))
# b = int(input("enter the number"))
# if a > b:
# 	print(a)
# else:
# 	print(b)
	
x = 12
y = 13
c = x
x = y
y = c
print(x)
print(y)

x = x + y 
y = x - y
x = x - y
print(x)
print(y)
