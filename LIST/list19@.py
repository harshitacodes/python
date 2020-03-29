char_list = ["a", "n", "t", "a", "a","a","c","d","f","g","h","j","k","m", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]    
new_list = []
i = 0 
while i < len(char_list):
    j = 0 
    add = 0
    index = char_list[i]
    c=[] 
    while j < len(char_list):
        if char_list[i] == char_list[j]:
            index = char_list[i]
            add = add + 1
        j = j + 1
    c.append(index)
    c.append(add)
    i = i + 1
    for var in range(len(new_list)):
    	if new_list[var][0] == c[0]:
     		break
    else:
     	new_list.append(c)

print(new_list)