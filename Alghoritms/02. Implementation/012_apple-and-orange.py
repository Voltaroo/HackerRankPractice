# Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Points: 10.00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    pos_a = list(map(int, apples))
    landing_pos_a = list(map(int, [a + pos_a[i] for i in range(len(pos_a))]))
    pos_b = list(map(int, oranges))
    landing_pos_b = list(map(int, [b + pos_b[i] for i in range(len(pos_b))]))
    
    res_x, res_y = 0, 0
    for i in range(len(landing_pos_a)):
        if s <= landing_pos_a[i] <= t:
            res_x += 1
        # print(landing_pos_a[i] if s <= landing_pos_a[i] <= t else print('X'))
    for i in range(len(landing_pos_b)):
        if s <= landing_pos_b[i] <= t:
            res_y += 1
        # print(landing_pos_b[i]) if s <= landing_pos_b[i] <= t else print('X')
    print(res_x)
    print(res_y)
    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
