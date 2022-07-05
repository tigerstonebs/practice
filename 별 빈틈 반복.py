va = 5
for val in range(va):  # 세로줄
    for i in range(va):  # 가로줄
        if val == 0 or val == 2 or val == 4 or i == 0 or i == 2 or i == 4:
            print("*", end="")
        else:
            (print(" ", end=""))
    print()
print()
j = 5
for val in range(j):  # 세로줄
    for i in range(j):  # 가로줄
        if val == i:
            print(" ", end="")
        else:
            print("*", end="")

    print()
