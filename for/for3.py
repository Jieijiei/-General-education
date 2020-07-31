a = 1 #数列
s = 0 #和
for n in range(10):
    s += a
    a = 2*a + 1

print(s)