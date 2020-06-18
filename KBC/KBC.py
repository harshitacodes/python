question_list = [
    "What is the capital of India?"            # doosra question
]
options_list = [
    #second question ke liye options
    "1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"]
i = 0
while i < len(question_list):
    print(question_list[0])
    j = 0
    while j < len(options_list):
        print(options_list[j])
        j = j + 1
    i = i + 1