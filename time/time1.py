from time import clock

flag = True

while flag:
    input("Press Enter to start.")

    t1 = clock()
    input("Press Enter in exactly 5 seconds.")
    t2 = clock()

    print(t2 - t1)

    result = abs(t2 - t1 - 5)
    if result < 0.01:
        print("Good Job!!".center(20))
    elif result < 0.5:
        print("So-so.".center(20))
    else:
        print("Too bad.".center(20))

    print()
    s = (input("Again? [y/n] >> "))
    if s == "n":
        flag = False

print("Good-bye.")