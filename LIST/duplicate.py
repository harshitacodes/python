# print only those nomber whicch has duplicates
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# for new duplicatelist
duplicate_list=[]
i=0
while i < len (n):
    j=i+1
    while j < len (n):
        if n[i]==n[j]:
            a=n[i]
            if n not in duplicate_list:
                if a in duplicate_list:
                    break
                duplicate_list.append(a)
                break
        j=j+1
    i=i+1    
#print one element of the duplicates  
print(duplicate_list)