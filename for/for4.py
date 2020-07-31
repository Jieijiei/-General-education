a = 1
s = 0
for n in range(1,11):#１０回
    s += a
    print(f"n={n:<2} a={a:<4} s={s}")
    a = 2*a + 1