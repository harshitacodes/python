# To seperate the data from the txt file by python code
my_file = open("people1-exercise.txt","r")
for data in my_file:
	if "delhi" in data:
		delhi_data = open("delhi.txt" , "a")
		delhi_data.write(data)
		# delhi data transfer into delhi.txt file
	elif "shimla" in data:
		shimla_data = open("shimla.txt" , "a")
		shimla_data.write(data)
		# shimle data transfer into shimla.txt file
	else:
		other_data = open("other.txt" , "a")
		other_data.write(data)
		# other data transfer into other.txt file


