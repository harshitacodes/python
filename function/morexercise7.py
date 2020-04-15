def common_numbers(list_1,list_2):
	duplicate_list=[]
	i=0
	while i < len (list_1):
		j=0
		while j < len (list_2):
			if list_1[i]==list_2[j]:
				a=list_1[i]
				if a not in duplicate_list:		
					duplicate_list.append(a)
			j=j+1
		i=i+1
	return duplicate_list
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
print(common_numbers(list1,list2)) 