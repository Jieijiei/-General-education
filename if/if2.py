cnt = 0#カウンタ

for x in range(1,101):

    if (x % 3 == 0) or ("3" in str(x)):
        s = str(x) + "!!" #バカになります<--面白い、ジャルジャル
    else:
        s = str(x)

    print(s.ljust(6), end="")

    cnt += 1#カウンタをインクリメント
    if cnt % 10 == 0:
        print()#１０個ごとに改行