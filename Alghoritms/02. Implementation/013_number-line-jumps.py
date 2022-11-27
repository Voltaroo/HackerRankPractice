# Problem: https://www.hackerrank.com/challenges/kangaroo/problem
# Points: 10.00


def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        return 'YES' if (x1 - x2) % (v1 - v2) == 0 else 'NO'
    return 'NO'