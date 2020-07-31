pn = 1#当たらない確率
for n in range(1, 500):
    pn *= 0.998#当たらない確率を0.99倍
    print(f'{n:<4}times --> {(1 - pn)*100:>4.2f}%')