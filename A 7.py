def sum_odds(n):
    total = 0 
    for i in range(1, n + 1, 2):
        total += i 
    return total