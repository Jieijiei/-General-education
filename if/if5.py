N= 1000

furui = [True] * (N + 1)

furui[0] = False
furui[1] = False

i = 2
while i**2 <= N:

    if furui[i]:
        j = i * i
        while j <= N:
            furui[j] = False
            j += i
    i += 1

cnt = 0
for p in range(1001):
    if furui[p]:
        cnt += 1
        print(f'{p:4}', end='')

        if cnt % 15 == 0:
            print()

print()
print()

cnt = 0
for p in range(10000001):
    if furui[p]:
        cnt += 1
        
        if cnt == 1000:
            print(f'1000番目の素数は{p}')

print(f'10,000,000までの素数は{cnt}個]')