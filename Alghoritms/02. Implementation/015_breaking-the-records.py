# Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Points: 10.00

def breakingRecords(scores):
    x = list(map(int, scores))
    g_min = g_max = 0
    v_min = v_max = x[0]
    for i in range(len(x)):
        if x[i] > v_max:
            v_max = x[i]
            g_max += 1
        if x[i] < v_min:
            v_min = x[i]
            g_min += 1
    
    return g_max, g_min
