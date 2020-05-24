# a = int(input("enter any number"))
# b = int(input("enter any number"))
# if a > b:
#     x = b
# else:
#     x = a
# i=1
# while i < x:
#     if (a % i == 0):
#         if (b % i == 0):
#             hcf=i
#     i = i + 1        
# print("hcf of both is",hcf)
    

# N = int(input())
# j = 0
# while j < N:
# 	a, b = map(int, input().split())	
# 	if a > b:
# 	    x = a
# 	else:
# 	    x = b
# 	i=1
# 	count = 0
# 	gcd = 1
# 	LCM = 1
# 	while i < x:
# 		if count ==0:
# 		    if (a % i == 0):
# 		        if (b % i == 0):
# 		        	LCM = LCM * i
# 		        	print(LCM)
	# 	        	count=count+1
	# 	else:
	# 	    if (a % i == 0):
	# 	        if (b % i == 0):
	# 	        	gcd = i
	# 	i = i + 1        
	# print("gcd of both is",gcd)
	# print("LCM of both is",LCM)
	# j = j + 1

# N = int(input())
# i = 0
# while i < N:
# 	a, b = map(int, input().split())	
# 	if a > b:
# 	    x = a
# 	else:
#  	    x = b
# 	j = 1  
# 	Lcm = 1  
# 	while j < x:
# 		if x % a == 0:
# 			if x % b == 0:
# 				Lcm = x
# 				print(Lcm)
# 		j = j + 1		
# 	# print(Lcm)	
# 	i = i + 1		
# N = int(input())
# i = 0
# while i < N:
# 	x, y = map(int, input().split())
# 	if x > y:
# 	   a = x
# 	else:
# 	   a = y
# 	while(True):
# 	   	if(a % x == 0):
# 	   		if (a% y == 0):
# 		   		lcm = a
# 		   		break
# 	   	a =a + 1
# 	print(lcm)   	
# 	i = i + 1

# N = int(input())
# i = 0
# lcm = 0
# coooo=0
# while i < N:
#     x, y = map(int, input().split())
#     if x > y:
#        a = x
#     else:
#        a = y
#     j = 1
#     while j < a/2:
#            if (x % j == 0):
#                if (y % j == 0):
#                    gcd = j
#            j = j + 1
#            print(j, "kjskj")
#     while (True):
#         if a % x == 0:
#             if (a% y == 0):
#             	print(a)
#             	lcm = a
#             	break   
        
        
#         a = a + 1      
#     print(gcd,lcm)

#     i = i + 1



X=int(input())
for i in range(0,X):
   x1,y1=map(int,input().split())
   x=x1
   y=y1
   while y1:
        x1, y1 = y1, x1%y1
   print(x1,end=" ")
   print(x*y//x1)



# def gcd(a,b):
#     if a==0:
#         return b
#     return gcd(b%a,a)
# t=int(input())
# for i in range(t):
#     l=input().split(" ")
#     a=int(l[0])
#     b=int(l[1])
#     g=gcd(a,b)
#     l=(a*b)//g
#     print(g,l)