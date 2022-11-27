# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Points: 10.00


def diagonalDifference(arr):
    
    tmp = list(map(list, arr))
    left_diagonal, right_diagonal = 0, 0
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            print(tmp[i][j])
    
    row_len = len(tmp[0]) - 1
    for x in range(len(tmp)):
        left_diagonal += tmp[x][x]
        right_diagonal += tmp[row_len - x][x]
    
    return abs(right_diagonal - left_diagonal)