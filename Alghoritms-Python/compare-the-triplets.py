# Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Points: 10.00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    
    x = list(map(int,a))
    y = list(map(int,b))
    
    
    res_alc = sum([(1 if x[i] > y[i] else 0) for i in range(len(x))])
    res_bob = sum([(1 if x[i] < y[i] else 0) for i in range(len(x))])
    
    
    return res_alc, res_bob
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    print(a,b)
    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
