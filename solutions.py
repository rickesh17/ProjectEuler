def problem_1(n):
    total = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def problem_2(n):
    l = [0, 1]
    next_value = sum(l[-2:])
    total = 0
    while next_value < n:
        if next_value % 2 == 0:
            total += next_value
        l.append(next_value)
        next_value = sum(l[-2:])
    return total