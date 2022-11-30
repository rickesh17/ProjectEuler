def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def CountFrequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def problem_5(n):
    all_p_factors = {}
    for i in reversed(range(1, n + 1)):
        p_factors = prime_factors(i)
        freq_dict = CountFrequency(p_factors)
        for k, v in freq_dict.items():
            if k in all_p_factors:
                if v > all_p_factors[k]:
                    all_p_factors[k] = v
            else:
                all_p_factors[k] = v
    smallest_multiple = 1
    for k, v in all_p_factors.items():
        smallest_multiple *= k ** v
    return smallest_multiple

# ============================================================
# ============================================================ 

def problem_4(start, end):
    largest_i = 0
    largest_j = 0
    largest_n = 0
    for i in range(start, end):
        for j in range(start, end):
            n = i * j
            reversed_n = int(str(n)[::-1])
            if n == reversed_n and n > largest_n:
                largest_i = i
                largest_j = j
                largest_n = n
    return largest_i, largest_j, largest_n

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

def problem_1(n):
    total = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total