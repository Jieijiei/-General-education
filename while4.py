i = 7
while i < 12:
    print(f'{i}'.rjust(3)
          + ' + '
          + f'{i*10}'.rjust(3)
          + ' =??')
    i += 1