def max_marks(list1):
	for i in range (0, len(list1)):
		max_list=list1[i][0]
		for j in range (len(list1[i])-1):
			if list1[i][j]<list1[i][j+1]:
				max_list = list1[i][j+1]
		print(max_list)		
marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [-87, -55, -1, -99]]
max_marks(marks)
