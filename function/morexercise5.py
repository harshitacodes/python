def factorial(number):
	mul = 1
	while  1 < number:
		mul =number * mul
		number = number - 1
	print(mul)
user_input = int(input("enter the number: "))	
factorial(user_input)	