#  program to print the sum of digits
a = int(input("enter the number"))
digit = 0
sum = 0
# logic
if(a<0):
	a = (-a)
while a > 0:
	digit = a % 10
	sum =  sum + digit
	a =  a // 10
# it will print the sum of digits
print(sum)
