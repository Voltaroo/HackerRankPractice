# Problem: https://www.hackerrank.com/challenges/a-very-big-sum/problem
# Points: 10.00


def aVeryBigSum(ar):
    converted = list(map(str, ar))
    sum = 0
    for i in range(len(converted)):
        sum += int(converted[i])
    
    return sum