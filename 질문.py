count = 1
while True:
    # 키보드로 입력
    inputNumber = int(input("정수 값을 입력하세요"))


# 입력 값 예외처리
    if inputNumber <= 0:
        print("양의정수를 입력하세요.")
        continue
# 20000이면 프로그램 종료
    elif inputNumber == 20000:
        break

# 입력 횟수와 입력 값 출력
    print(count, "번쨰 입력: ", inputNumber)
    count += 1


# 짝수 또는 홀수 판별후 출력
    if inputNumber % 2 == 0:
        print("\t\t짝수입니다")
    else:
        print("\t\t홀수입니다")

# 3의 배수 판별후 출력
    if inputNumber % 3 == 0:
        print("\t\t3의 배수 입니다.")


# 7의 배수 판별후 출력
    if inputNumber % 7 == 0:
        print("\t\t7의 배수 입니다.")
