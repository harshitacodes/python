def password(number):
	if len(number) <=16 and len(number)>=6:
		if ("$" in number) and (("A" or "Z") in number) and (("2" and "8") in number): 
			print("nice your passwordis too strong")
		else:
			print("oops few characters are missing.... its a weak password")
	else:
		print("length should be between 6 to 16")
pass_word= input("enter your password: ")
password(pass_word)					 