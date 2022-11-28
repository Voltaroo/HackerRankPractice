# Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Points: 10.00


def birthday(s, d, m):
    print('Chocolate:', s, '\nLooking for pieces of',
          d, '\nNumber of iterations:', m)
    res = 0

    if len(s) == 1:
        return 1 if s[0] == d else 0

    for i in range(len(s)-m + 1):
        ctn = 0
        for j in range(i, i+m):
            ctn += s[j]
        if ctn == d:
            res += 1
            print('X')
        else:
            pass

    return res
