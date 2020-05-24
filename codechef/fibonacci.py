# # program to print the n finobacci series
# def fibonacciSeries(number):
# 	n1 = 0
# 	n2 = 1
# 	sum = 0
# 	count = 1
# 	while(count <= number):
# 	  print(sum)
# 	  count = count + 1
# 	  n1 = n2
# 	  n2 = sum
# 	  sum = n1 + n2    
# userInput = int(input("Enter the number: "))  
# fibonacciSeries(userInput)



# def sorttheList(myList):
# 	newList = []
# 	while myList:
# 	    minimum = myList[0]
# 	    minimum_index = 0  
# 	    for i in range (len(myList)): 
# 	        if myList[i] < minimum:
# 	        	minimum_index = i
# 	        	minimum = myList[i]
# 	    newList = newList + [myList[i]]
# 	    myList[:minimum_index] + myList[minimum_index + 1:]
# 	    # myList.remove(minimum) 
# 	return newList     
# unsortedList = [[-15,-26,15,1,23,-64,23,76],[12,13,7,45,6,1,0],[89,56,23,13,89]]     
# sortedList = []

# for oneList in unsortedList:
# 	anotherSortedlist = sorttheList(oneList)
# 	sortedList = sortedList + [anotherSortedlist]

# print(sortedList)


# N = int(input())
# i = 0
# while i < N:
# 	my_list = int(input())
# 	i = i + 1
# 	new_list = ""
# 	while my_list:
# 		i = 0
# 		while i < len(my_list):
# 		    min = my_list[i]  
# 		    for x in my_list: 
# 		        if x < min:
# 		            min = x
# 		    new_list = new_list + str(min)
# 		    my_list.remove(min) 
# 		    i = i + 1     
# 	print(new_list)



N = int(input())
j = 0
number = []
while j < N:
	n = int(input())
	number.append(n)
	j = j + 1
n=0
while n<len(number):
    i=0
    while i<len(number)-1:
        if number[i] > number[i+1]:
            number[i],number[i+1]=number[i+1],number[i]
        else:
            number[i],number[i+1]=number[i],number[i+1]
        i=i+1
    n=n+1
t = 0
while t < len(number):
	print(number[t])
	t = t + 1 