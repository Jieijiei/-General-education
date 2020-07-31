for x in range(1, 6):

    print(f'{x}**n || ', end='')
    for n in range(1, 6):
        l = len(str(5 ** n)) + 1
        print(f'{x**n}'.ljust(l) + '| ', end='')

    print()