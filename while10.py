i = 1
while i <= 9:
    j = 1
    while j <= 9:
        print(str(i * j).rjust(3), end='')
        j += 1
    
    print()
    i += 1