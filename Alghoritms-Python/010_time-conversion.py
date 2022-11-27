# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Points: 15.00

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hours = s[0:2]
    result_time = s[2:-2]
    t_format = s[-2:]
    
    print('Format:',t_format,'\nHours:',hours,'\nRest of the input:',result_time)
    if int(hours) > 12:
        return
    if t_format == 'PM':
        hours_alt = '12' if hours == '12' else str(int(hours) + 12)
        return hours_alt + result_time
    if t_format == 'AM':
        hours_alt = '00' if hours == '12' else hours
        return hours_alt + result_time
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
