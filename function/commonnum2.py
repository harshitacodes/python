def common_numbers(list_1,list_2):
	new_list = []
	for i in list_1:
		if i not in new_list:
			new_list.append(i)
			for j in list_2:
				if j not in new_list:
					new_list.append(j)
	return new_list
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
print(common_numbers(list1,list2))
