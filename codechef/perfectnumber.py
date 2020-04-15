num = int(input(" entr the number to know , it perfect number or not: "))
a = 2
sum = 0
while a * a <= num:
	if num % a == 0:
		if a == num/a:
			sum = sum + a
		else:
			sum = sum + a + num/a
	a = a + 1
else:
	sum = sum + 1
	if sum == num:
		print("perfect num")
	else:
		print("not perferct")					
