# def decimalToBinary(num):
#     if num > 1:
#         decimalToBinary(num // 2)
#     print(num % 2, end="")


# # decimal number
# number = int(input())

# decimalToBinary(number)

 
# T = int(input())
# i = 0
# while i < T:
# 	t = int(input())
# 	j = 0
# 	result = ""
# 	while t:
# 		remainder = t % 2
# 		div = t//2
# 		t = div
# 		result = result + str(remainder)
# 	a = result[::-1]	
# 	print(a)	
# 	i = i + 1
	

N = int(input())
j = 0
number = []
while j < N:
	n = int(input())
	number.append(n)
	j = j + 1
n=0
while n<len(number):
    i=0
    while i<len(number)-1:
        if number[i] > number[i+1]:
            number[i],number[i+1]=number[i+1],number[i]
        else:
            number[i],number[i+1]=number[i],number[i+1]
        i=i+1
    n=n+1
t = 0
while t < len(number):
	print(number[t])
	t = t + 1 
