# program will print the reverse of any number
# a = int(input("enter the number to get the reverse"))
# # n = 1
# # string = ""
# while a>0:
# 	string = string + str(a%10)
# 	a = a//10
# print (string)

# num,reverse,b,c=a,0,0,1
# if(a<0):
# 	a = (-a)
# 	num = (-num)
# 	while num>0:
# 		c=c*10
# 		num=num//10
# 	c=c//10
# 	while a > 0:
# 	    reverse = a % 10 
# 	    b= b + (reverse*c)
# 	    a = a//10
# 	    c=c//10
# 	print(b)
# else:
# 	while num>0:
# 		c=c*10
# 		num=num//10
# 	c=c//10
# 	while a > 0:
# 	    reverse = a % 10 
# 	    b= b + (reverse*c)
# 	    a = a//10
# 	    c=c//10
# 	print(b)	 
    

# num = int(input("Enter your favourite number: "))
 
# # Initiate value to null
# test_num = 0
 
# # Check using while loop
 
# while(num>0):
#   #Logic
#   remainder = num % 10
#   test_num = (test_num * 10) + remainder
#   num = num//10

# print(test_num)


# n = int(input("enter the number"))
# x = 0
# if n < 0:
# 	n = (-n)
# 	while n > 0:
# 		x = (x*10) +(n % 10)
# 		n = n // 10
# 	print(x)	 
# else:
# 	while n > 0:
# 		x = (x*10) +(n % 10)
# 		n = n // 10
# 	print(x)



# more optimized , to  print the reverse of the number
n = int(input("enter the number"))
x = 0
if n < 0:
	n = (-n) 
while n > 0:
	x = (x*10) +(n % 10)
	n = n // 10
print(x)