# Problem: https://www.hackerrank.com/challenges/grading/problem
# Points: 10.00


def gradingStudents(grades):
    tmp = list(map(int, grades))
    
    for i in range(len(tmp)):
        next_closest = (tmp[i] // 5) * 5 + 5
        difference = next_closest - tmp[i]
        if next_closest >= 40 and difference < 3:
            tmp[i] = next_closest
    
    return tmp