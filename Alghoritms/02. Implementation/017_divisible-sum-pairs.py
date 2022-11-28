# Problem: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
# Points: 10.00

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    return count