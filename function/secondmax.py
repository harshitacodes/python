def number(num1,num2,num3):
	if (num1>num2):
		if(num1>num3):
			print(num1)
		else:
			print(num3)
	elif(num2>num3):
		print(num2)
	else:
		print(num3)
number1=int(input("enter the number"))
number2=int(input("enter the number"))
number3=int(input("enter the number"))
number(number1,number2,number3)			