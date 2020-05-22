i = 7
while i < 12:
    print(f'{i}'.ljust(3)
          + ' + '
          + f'{i*10}'.ljust(3)
          + ' =??')
    i += 1