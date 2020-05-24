# n = int(input("enter the number"))
# i = 0
# while i < n:
# 	num = int(input("enter the number"))
# 	if num % 2 == 0:
# 		print("even")
# 	else:
# 		print("odd")	
# 	i = i + 1	


N = int(input("enter the number"))
res = 1
p = 2
while p <= N:
	c = 0 
	while N % p == 0:
		c = c +  1
		N = N // p
	
	res = res * (c + 1)
	print(res)
	p = p + 1	
print(res)	