
question_list = [
    "Q-I. How many continents are there?",  #first question
	"Q-II. What is the capital of India?",   #second question
	"Q-III. NG mei kaun se course padhaya jaata hai?"  #third question
]
options_list = [
      #options of first questions
	["1.Four", "2.Nine", "3.Seven", "4.Eight"],
	#options of second questions
	["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
	#options of third questions
	["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
	]
i = 0
while i < len(question_list):
	print(question_list[i])
	j = 0
	while j < len(options_list):
		if i == j:
			k = 0
			while k < len(options_list[j]):
				print(options_list[j][k])
			k = k + 1
			break
		j = j + 1
	i = i + 1	
