# t=int(input())
# for i in range(t):
#     a,b,k=map(int,input().split())
#     s=a+b
#     ma=s*4
#     if a<=2*b:
#         m=b*4
#     else:
#         m=b*4 +(a-2*b)*4
#     if k>=m and k<=ma and k%4==0:
#             print("yes")
#     else:
#                 print("no")



# t=int(input())
# for i in range(t):
    
#  c,d,l = map(int,input().split())
#  maximum=d*4
#  if l<4:
#      print("no")
#  elif l%4!=0:
#      print("no")
#  elif l>4*d+4*c:
#      print("no")
#  elif l<4*d:
#      print("no")
#  elif c<d*2:
#      if maximum==l:
#          print("yes")
#      for i in range(c):
#         maximum=maximum+4
#         if maximum==l:
#             print("yes")
            
 # elif c>d*2:
 #     a=c-(d*2)
 #     b=c-a
 #     a=4*a 
 #     maximum=maximum+a
 #     if maximum==l:
 #         print("yes")
 #     for i in range(b):
 #      maximum=maximum+4
 #      if maximum==l:
 #         print("yes")
         
 # else:
 #     print("no")



t=int(input())
for i in range(t):
    c,d,l=map(int,input().split())
    s=c+d
    mc=s*4
    if c<=2*d:
        m=d*4
    else:
        m=d*4 +(c-2*d)*4
    if l>=m and l<=mc and l%4==0:
            print("yes")
    else:
                print("no")
            
