def break_into_words(list1):
	for i in list1:
	    sentence_list = []
	    word = ''
	    for i in list1:
	        if i == ' ':
	            sentence_list.append(word)
	            word = ''
	        else:
	            word = word + i
	    if word != '':
	    	sentence_list.append(word)
	return sentence_list    
sentance = "NavGurukul is an alternative"	
print(break_into_words(sentance))	
