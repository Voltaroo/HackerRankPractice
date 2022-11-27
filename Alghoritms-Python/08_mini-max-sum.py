# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Points: 10.00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sort_min = sorted(arr)

    sum_min = sum([sort_min[i] for i in range(0,len(sort_min) - 1)])
    sum_max = sum([sort_min[i] for i in range(1,len(sort_min))])
        
    print(sum_min, sum_max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
