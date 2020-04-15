# import math

# factors = int(input("enter the number to get the factors"))
# i = 1
# while i <= math.sqrt(factors):
# 	if factors % i == 0 :
# 		if i == factors/i:
# 			print(i)
# 		else:
# 			print(i, "," ,int(factors/i))
# 	i = i + 1

# 			
a =  int(input("entr the number to get the factors"))
i = 1
while i * i<= a:
	if a % i == 0:
		if i == a //i:
			print (i)
		else:
			print( i , "," ,(a//i))
	i = i + 1			