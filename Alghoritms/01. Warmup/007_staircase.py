# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Points: 10.00


def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)