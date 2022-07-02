for i in range(3):  # 세로줄 반복
    for va in range(i):
        print(" ", end="")
    for j in range(-2*i+5):
        if i == 0 or j == 2 or j == 0 or i == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(2):  # 세로줄 반복
    if i == 0:
        print(" ", end="")
    for j in range(2*i+3):
        if j == 0 or j == 3 or j == 2 or i == 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
