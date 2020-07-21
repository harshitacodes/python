def break_into_words(list1):
	my_list = []
	s = ''
	for i in list1:
		if i != ' ':
			s = s + i
		else:
			my_list = my_list + [s]
			s = ''
	my_list =  my_list + [s]
	return my_list
sentance = "NavGurukul is an alternative"	
print(break_into_words(sentance))	
