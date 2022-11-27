# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Points: 10.00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    tallest_candle = max(candles)
    count_tallest = sum([1 if candles[i] == tallest_candle else 0 for i in range(len(candles))])
    return count_tallest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
