banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
my_file = open("file-question3.txt", "w")
for i in banks_list:
	my_file.write(i)
	my_file.write("\n")
my_file.close()	
