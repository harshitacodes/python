num_list=[24, 33, 44, 5, 21, 19, 23, 30]
print("unsorted list:",num_list)
for j in range (len(num_list)-1,0,-1):
	for i in range (j):
		if num_list[i]>num_list[i+1]:
			num_list[i],num_list[i+1]=num_list[i+1],num_list[i]
			list2=num_list
	else:
		list1=num_list
print("sorted list:",num_list)





num_list=[24, 33, 44, 5, 21, 19, 23, 30]
print("unsorted list:",num_list)
for j in range (len(num_list)-1,0,-1):
	for i in range (j):
		if num_list[i]>num_list[i+1]:
			num_list[i],num_list[i+1]=num_list[i+1],num_list[i]
			list2=num_list
	else:
		list1=num_list
print("sorted list:",num_list)
