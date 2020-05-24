# N = int(input("enter the number of soldiers: "))
# count_weapons = []
# index = 0
# while index < N:
#     weapons_input = int(input("enter the number of weapeans: "))
#     count_weapons.append(weapons_input)
#     index=index+1
# iterate = 0 
# odd_count = 0
# even_count = 0
# while iterate < len(count_weapons):
#     if count_weapons[iterate] % 2 == 0:
#         even_count = even_count + 1
#     else:
#         odd_count = odd_count + 1
#     iterate = iterate + 1
# if even_count > odd_count:
#     print("READY FOR BATTLE")
# else:
#     print("NOT READY")        


# N = int(input("enter the number of soldiers: "))
# i = 0
# while i < N:
#     n = map(int,input().split())
#     i = i + 1
#     iterate = 0 
#     odd_count = 0
#     even_count = 0
#     while iterate < len(n):
#         if count_weapons[iterate] % 2 == 0:
#             even_count = even_count + 1
#         else:
#             odd_count = odd_count + 1
#         iterate = iterate + 1
#     if even_count > odd_count:
#         print("READY FOR BATTLE")
#     else:
#         print("NOT READY")  


# N= int(input())
# l=list(map(int,input().split()))
# lucky=0
# unlucky=0
# i = 0
# while i < len(l):
#     if i%2==0:
#         lucky=lucky + 1
#     else:
#         unlucky=unlucky + 1
#     i = i + 1    
# if lucky>unlucky:
#     print("READY FOR BATTLE")
# else:
#     print("NOT READY")      

n = int(input()) 
i = 0
while i < n:
    T = input()
    B = T.split()
    # print(B)
    a = int(B[0])
    b = int(B[1])
    C = a % b
    print(C)
    i = i + 1