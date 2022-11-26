# Problem: https://www.hackerrank.com/challenges/plus-minus/problem
# Points: 10.00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    tmp = list(map(int,arr))
    sum_nega = sum([(1 if arr[i] > 0 else 0) for i in range(len(tmp))])
    sum_posi = sum([(1 if arr[i] < 0 else 0) for i in range(len(tmp))])
    sum_zero = sum([(1 if not arr[i] else 0) for i in range(len(tmp))])
    
    print('{:.6f}'.format(sum_nega/len(tmp)))
    print('{:.6f}'.format(sum_posi/len(tmp)))
    print('{:.6f}'.format(sum_zero/len(tmp)))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
