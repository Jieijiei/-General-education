cnt = 0

for x in range(1, 51):
    for y in range(x, 51):
        for z in range(y, 51):
            if x**2 + y**2 == z**2:
                cnt += 1
                print(f'{cnt:2}: ({x:2}, {y:2}, {z:2})')