p = 1.0
for n in range(1, 51):
    print(f'n={n:<2}: {1 - p:<.4f}')
    p *= (365 - n) / 365