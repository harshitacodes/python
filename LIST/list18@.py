#seperate the odd and even elements from the given list:
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
#two list for store odd and even elements
odd_list=[]
even_list=[]
sum_odd=0
sum_even=0
sum_elements=sum_odd+sum_even
while counter<len(elements):
    if elements[counter]%2!=0:
        odd=elements[counter]
        #add odd value in this list
        odd_list.append(odd)
        # print(odd_list)
        sum_odd=elements[counter]+sum_odd
        # sum of the odd number
    else:
        even=elements[counter]
        #add even value in this list
        even_list.append(even)
        # print(even_list)
        sum_even=elements[counter]+sum_even
        # sum of the even number
    counter=counter+1    
# print("odd"+str(odd_list))
# print("even"+str(even_list))
print("count of elements",len(elements))
print("count of odd",len(odd_list))
print("count of even",len(even_list))
print("sum of odd",sum_odd)
print("sum of even",sum_even)
print("sum of elements",sum_odd+sum_even)
print("average of elements",int(sum_elements/len(elements)))
print("average of odd number",int(sum_odd/len(odd_list)))
print("average of even number",int(sum_even/len(even_list)))