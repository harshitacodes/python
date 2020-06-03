def harshad_nummber(num):
	x = [int(i) for i in str(num)]
	sum1=0
	for i in x:
		sum1 = i +sum1
	if num % sum1 == 0:
		print(num)
for i in range(1, 1001):
	harshad_nummber(i)