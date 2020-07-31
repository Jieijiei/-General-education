a = [1] #初項
for n in range(9):#９回
    a += [2*a[n] + 1]

print(a)
print(sum(a))