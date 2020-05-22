n = 2017
repuni = 1
while repuni % n != 0:
    repuni *= 10
    repuni += 1

print(repuni)
print(len(str(repuni)))