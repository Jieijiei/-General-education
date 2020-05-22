N = 3333
result = '' #結果保存用の文字列

while N >1:
    result = str(N % 2) + result
    N //= 2 #２で割って切り捨て

result = str(N % 2) + result
print(result)