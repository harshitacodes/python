# num = int(input(" enter the number to know , it perfect number or not: "))
# a = 2
# sum = 0
# while a * a <= num:
# 	if num % a == 0:
# 		if a == num/a:
# 			sum = sum + a

# 		else:
# 			sum = sum + a + num/a
# 	a = a + 1
# else:
# 	# sum = sum + 1
# 	print(sum)
# 	if sum == num:
# 		print("perfect num")
# 	else:
# 		print("not perferct")					






N = int(input())
i = 0
while i < N:
    n= int(input())
    a = 2
    sum = 0
    while a * a <= n:
    	if n % a == 0:
    		if a == n/a:
    			sum = sum + a
    		else:
    			sum = sum + a + n/a
    	a = a + 1
    else:
    	sum = sum + 1
    	if sum == 1:
    	    print("NO")
    	elif sum == n:
    		print("YES")
    	else:
    		print("NO")					
    i = i + 1
