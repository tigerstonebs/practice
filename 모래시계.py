value = 11
for i in range(value):  # 세로로 5번을 출력

    for j in range(value):  # 가로로 5번을 출력
        if i == j or i+j == value-1 or i == 0 or i == value-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
