list=[24, 33, 44, 5, 21, 19, 23, 30]
print("unsorted list:",list)
for j in range (len(list)-1,0,-1):
	for i in range (j):
		if list[i]>list[i+1]:
			list[i],list[i+1]=list[i+1],list[i]
			list2=list
	else:
		list1=list
print("sorted list:",list)
