# Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
# Points: 10.00


def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    pos_a = list(map(int, apples))
    landing_pos_a = list(map(int, [a + pos_a[i] for i in range(len(pos_a))]))
    pos_b = list(map(int, oranges))
    landing_pos_b = list(map(int, [b + pos_b[i] for i in range(len(pos_b))]))
    
    res_x, res_y = 0, 0
    for i in range(len(landing_pos_a)):
        if s <= landing_pos_a[i] <= t:
            res_x += 1
        # print(landing_pos_a[i] if s <= landing_pos_a[i] <= t else print('X'))
    for i in range(len(landing_pos_b)):
        if s <= landing_pos_b[i] <= t:
            res_y += 1
        # print(landing_pos_b[i]) if s <= landing_pos_b[i] <= t else print('X')
    print(res_x)
    print(res_y)