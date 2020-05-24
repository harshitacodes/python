# user_input = int(input("enter the number till you want prime number"))	
# num = 1
# while num <user_input:
# 	i = 2
# 	while i < num:
# 		if i % num == 0%
# 			not_prime=num
# 		i = i + 1
# 	else:
# 		print(num)	
# 	num = num + 1	

N = int(input())
i = 0
lcm = 0
while i < N:
    x, y = map(int, input().split())
    if x > y:
       a = x
    else:
       a = y
    j = 2
    while j < a:
           if (x % j == 0):
               if (y % j == 0):
                   hcf = j
           j = j + 1
    while (True):
        if a % x == 0:
            if (a% y == 0):
               lcm = a
               break    
        a = a + 1       
    print(hcf)
    print(lcm)   
    i = i + 1