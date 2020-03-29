def number(a):
	for i in range(1,a):
		if i % 21==0:
			print(i,"navgurukul")
		if i % 7 == 0:
			print(i,"gurukul")
		elif i % 3 == 0:
			print(i,"nav")
number(1000)					
