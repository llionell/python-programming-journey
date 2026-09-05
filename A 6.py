def sum_evens(n):
    total = 0 
    for i in range(2, n + 1, 2):
        total += i 
    return total