N = int(input("Input an integer N: "))
flag = True#判定のためのフラグ

#2の倍数だけ別処理
if N % 2 == 0 and N != 2:
    flag = False

k = 3
while k**2 <= N and flag:
    if N % k == 0:
        flag = False
    k += 2#偶数は調べなくて良い.

if flag:
    print(f"{N} is prime.")
else:
    print(f"{N} is not prime.")