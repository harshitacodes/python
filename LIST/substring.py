mainStr = "the quick brown fox jumped over the lazy dog the dog slept over the verandah."
newStr = mainStr.split(" ")
i=0
a = ""
while i < len(newStr):
	if newStr[i] == "over":
		a = a+  "on" + " "
	else:
		a = a + newStr[i] + " "
	i = i + 1		
print(a)