# user_input = input("Please Enter Your Own String : ")
# vowels = 0
# consonants = 0

# for i in user_input:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
#        or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#         vowels = vowels + 1
#     else:
#         consonants = consonants + 1

# print("Vowels = ", vowels)

# print("Consonants = ", consonants)



# vowels = "aeiouAEIOU"
# a = input("enter the string you want ")
# i = 0
# new = ''
# while i < len(a):
# 	if a[i]!= " ":
# 		new = new + a[i]
# 	i = i + 1
# l = len(new)
# count_vowel = 0
# consonants = 0 
# i = 0
# while i < len(new):
# 	j = 0
# 	while j < len(vowels):
# 		if new[i] == vowels[j]:
# 			count_vowel = count_vowel + 1
# 		j = j + 1
# 	i = i + 1
# print(count_vowel)
# consonants = l - count_vowel
# print(consonants)			


# vowels = "aeiouAEIOU"
# consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# vow = 0
# const = 0
# a = input("enter the string")
# i = 0 
# while i < len(a):
# 	j = 0
# 	while j < len(vowels):
# 		if a[i] == vowels[j]:
# 			vow = vow + 1
# 		else:
# 			print("", end = "")	
# 		j = j + 1
# 	k = 0	
# 	while k < len(consonants):
# 		if a[i] == consonants[k]:
# 			const = const + 1
# 		else:
# 			print("", end = "")
# 		k = k +	
# 	i = i + 1
# print(vow)
# print(const)


vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vow = 0
const = 0
a = input("enter the string ")
i = 0 
while i < len(a):
	w = "not vowel"
	j = 0
	while j < len(vowels):
		if a[i] == vowels[j]:
			vow = vow + 1
			w = "vowel"
			break
		j = j + 1
	if w == "not vowel":
		k = 0
		while k < len(consonants):
			if a[i] == consonants[k]:
				const = const + 1
				break
			k = k + 1	
	i = i + 1
print(vow)
print(const)




		

