#do lists pe ek saath kaise iterate krenge
students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
counter=0
while counter<len(students):
	#changing the type of sencond list(marks)
    print(students[counter]+str(marks[counter]))
    counter=counter+1