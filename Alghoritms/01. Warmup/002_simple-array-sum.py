# Problem: https://www.hackerrank.com/challenges/simple-array-sum/problem
# Points: 10.00


def simpleArraySum(ar):
    sum = 0
    for a in ar:
        sum += a
    return int(sum)