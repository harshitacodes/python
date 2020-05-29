magic_square = [
    [5, 3, 7],
    [1, 8, 9],
    [6, 4, 2]
]
sum0=(magic_square[0][0]+magic_square[0][1]+magic_square[0][2])
sum1=(magic_square[1][0]+magic_square[1][1]+magic_square[1][2])
sum2=(magic_square[2][0]+magic_square[2][1]+magic_square[2][2])
diagnol1=(magic_square[0][0]+magic_square[1][1]+magic_square[2][2])
diagnol2=(magic_square[0][2]+magic_square[1][1]+magic_square[2][0])
if sum0==sum1==sum2==diagnol1==diagnol2:
    print("valid magic_square")