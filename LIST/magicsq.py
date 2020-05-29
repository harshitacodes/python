magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
while i<len(magic_square):
 	sum=0
 	c=0
 	while c<len(magic_square[i]):
 		sum=sum+magic_square[i][c]
 		c=c+1
 	print(sum/len(magic_square[i]))
 	i=i+1