#seperate the odd and even elements from the given list:
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
#two list for store odd and even elements
odd_list=[]
even_list=[]
sum_odd=0
sum_even=0
while counter<len(elements):
    if elements[counter]%2!=0:
        odd=elements[counter]
        #add odd value in this list
        odd_list.append(odd)
        # print(odd_list)
        sum_odd=elements[counter]+sum_odd
    else:
        even=elements[counter]
        #add even value in this list
        even_list.append(even)
        # print(even_list)
        sum_even=elements[counter]+sum_even
    counter=counter+1    
print("odd"+str(odd_list))
print("even"+str(even_list))  
odd=len(odd_list)
even=len(even_list)
print(sum_odd)
print(sum_even)	
print(int(sum_odd/len(odd_list)))
print(int(sum_even/len(even_list)))