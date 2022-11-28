def problem_1(n):
    total = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# ============================================================
# ============================================================ 

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

# ============================================================
# ============================================================ 

def modulo(divider, n):
    if n % divider == 0:
        return int(n / divider)
    else:
        return n
    
def smallest_factor(n):
    i = 2
    res = modulo(i, n)
    while res == n:
        i += 1
        res = modulo(i, n)
    return i, res

def problem_3(n):
    factors = []
    factor, res = smallest_factor(n)
    factors.append(factor)
    while res != 1:
        factor, res = smallest_factor(res)
        factors.append(factor)
    return factors

# ============================================================
# ============================================================ 

