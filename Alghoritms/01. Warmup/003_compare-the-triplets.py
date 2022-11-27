# Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Points: 10.00


def compareTriplets(a, b):
    
    x = list(map(int,a))
    y = list(map(int,b))
    
    res_alc = sum([(1 if x[i] > y[i] else 0) for i in range(len(x))])
    res_bob = sum([(1 if x[i] < y[i] else 0) for i in range(len(x))])
    
    return res_alc, res_bob