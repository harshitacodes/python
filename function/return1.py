def calculator(number_x,number_y,operation):
	if operation =="addition":
		addition= number_x+number_y
		return addition
	elif operation =="subtraction":
		subtraction= number_x - number_y
		return subtraction
	elif operation == "multiply":
		multiply= number_x*number_y
		return multiply
	elif operation=="divide":
		divide= number_x/number_y
		return divide
number_1 = int(input("enter any number: "))
number_2 = int(input("enter any number: "))
operation1 = input("enter the operatin: ")
print(calculator(number_1,number_2,operation1))		
