val = 5
for i in range(val):
    for j in range(4-i):
        print(" ", end="")
    for va in range(2*i+1):
        if va == 0 or i == val-1 or va == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
