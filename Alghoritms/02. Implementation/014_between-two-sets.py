# Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
# Points: 10.00

def getTotalX(a, b):
    x = list(map(int, a))
    y = list(map(int, b))
    
    count = 0
    
    for i in range(max(x), min(y) + 1):
        is_f = True
        for t in x:
            if i % t != 0:
                is_f = False
                break
        for t in y:
            if t % i != 0:
                is_f = False
                break
        
        count = count + 1 if is_f else count    
    
    return count
            
