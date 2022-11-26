# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Points: 10.00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    tmp = list(map(list,arr))
    left_diagonal, right_diagonal = 0, 0
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            print(tmp[i][j])
    
    row_len = len(tmp[0]) - 1
    for x in range(len(tmp)):
        left_diagonal += tmp[x][x]
        right_diagonal += tmp[row_len - x][x]
    
    return abs(right_diagonal - left_diagonal)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
