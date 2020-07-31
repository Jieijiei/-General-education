print("Please input your score.")
tokuten = int(input(">>> "))

if tokuten >= 80:
    seiseki = 5
elif tokuten >= 65:
    seiseki = 4
elif tokuten >= 45:
    seiseki = 3
elif tokuten >= 25:
    seiseki = 2
else:
    seiseki = 1

print(f"Your grade is {seiseki}")