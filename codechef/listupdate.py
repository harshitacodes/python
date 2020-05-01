# i = 0
# new_list = []
# while i < 10:
# 	user = int(input("enter the number"))
# 	new_list.append(user)
# 	i = i + 1
# second_list = []	
# j = 0	
# while j < len(new_list):
# 	if new_list[j] % 2 == 0:
# 		num = new_list[j] * 100
# 		second_list.append(num)
# 	else:
# 		num = new_list[j] * (-1)
# 		second_list.append(num)
# 	j = j + 1
# print(second_list)		
			


i = 0
new_list = []
while i < 10:
	user = int(input("enter the number"))
	if user % 2 == 0:
		num = user * 100
		new_list.append(num)
	else:
		num = user * (-1)
		new_list.append(num)
	i = i + 1
print(new_list)	

