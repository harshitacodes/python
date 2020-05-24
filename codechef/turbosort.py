# N = int(input())
# i = 0
# number = ""
# while i < N:
# 	n = input()
# 	number = number + n
# 	i = i + 1

# n=0
# while n<len(number):
#     i=0
#     while i<len(number)-1:
#     	if int(number[i]) > int(number[i+1]):
#     		number=number[:i]+number[i+1]+number[i+1:]
#     		print(number)
#     		number=number[:i-1]+number[i]+number[i+1:]
#     		print(number, "ygyg")
#     	i=i+1
#     n=n+1



# number = [-2,45,0,-8,11,-9,2]
# n=0
# while n<len(number):
#     i=0
#     while i<len(number)-1:
#         if number[i] > number[i+1]:
#             number[i],number[i+1]=number[i+1],number[i]
#         i=i+1
#     n=n+1
# print(number)


# N = int(input())
# j = 0
# number = []
# while j < N:
# 	n = int(input())
# 	number.append(n)
# 	j = j + 1
# n=0
# while n<len(number):
#     i=0
#     while i<len(number)-1:
#         if number[i] > number[i+1]:
#             number[i],number[i+1]=number[i+1],number[i]
#         else:
#             number[i],number[i+1]=number[i],number[i+1]
#         i=i+1
#     n=n+1
# t = 0
# while t < len(number):
# 	print(number[t])
	# t = t + 1 
# number = [-2,45,0,-8,11,-9,2]
# n=0
# while n<len(number):
#     i=0
#     while i<len(number)-1:
#         if number[i] > number[i+1]:
#             number[i],number[i+1]=number[i+1],number[i]
#         else:
#             number[i],number[i+1]=number[i],number[i+1]
#         i=i+1
#     n=n+1
# print(number)

# n=int(input())
# m=[]
# for i in range(n):
#     m.append(int(input()))
# z=sorted(m)
# for i in z:
#     print(i)


# t = int(input())

# list = []
# for i in range(t):
#     list.append(int(input()))
    
# list = (sorted(list))

# for i in range(len(list)):
#     print(list[i])

a = int(input())
total = []
for i in range(a):
    b = int(input())
    total.append(b)
total.sort()
for j in total:
    print(j)