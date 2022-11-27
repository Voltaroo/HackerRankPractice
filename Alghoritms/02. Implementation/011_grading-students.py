# Problem: https://www.hackerrank.com/challenges/grading/problem
# Points: 10.00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    tmp = list(map(int,grades))
    
    for i in range(len(tmp)):
        next_closest = (tmp[i] // 5) * 5 + 5
        difference = next_closest - tmp[i]
        if next_closest >= 40 and difference < 3:
            tmp[i] = next_closest
    
    return tmp
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
