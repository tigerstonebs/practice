row = int(input("양의 정수를 입력하세요."))

for i in range(1, row+1):
    for j in range(i):
        print(j+1, end=" ")
    print()
