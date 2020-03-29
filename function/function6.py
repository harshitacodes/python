def check_number(a,b):
	if a % 2 == 0:
		if b % 2 == 0:
			print("dono even hai")
		else:
			print("dono even nhi hai")
	else:
		print("dono even nhi hai")
user_input1=int(input("enter any number:"))
user_input2=int(input("enter any number:"))	
check_number(user_input1,user_input2)			