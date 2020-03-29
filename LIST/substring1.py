mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
i=0
new_str=[]
while i < len(mainStr):
	if mainStr[i]=="over":
		break
		add=mainStr[i]
		new_str.append(add)
	i=i+1
print(new_str)
