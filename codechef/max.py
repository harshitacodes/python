#To print the maximum number in three input
num1=int(input("put any number"))
num2=int(input("put any number"))
num3=int(input("put any number"))
if (num1>num2):
    if(num1>num3):
        print(num1)
    else:
        print(num3)
elif(num2>num3):
    print(num2)
else:
    print(num3)
    