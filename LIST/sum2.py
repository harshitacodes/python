marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
i=0
sum=0
while i<len(marks):
	c=0
	while c<len(marks[i]):
		sum=sum+marks[i][c]
		c=c+1
	i=i+1
print(sum)	 