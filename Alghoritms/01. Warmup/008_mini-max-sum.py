# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Points: 10.00


def miniMaxSum(arr):
    sort_min = sorted(arr)

    sum_min = sum([sort_min[i] for i in range(0, len(sort_min) - 1)])
    sum_max = sum([sort_min[i] for i in range(1, len(sort_min))])
        
    print(sum_min, sum_max)