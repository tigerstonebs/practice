
while True:
    # 메뉴 우선 출력후 기보드로부터 정수값 출력
    inputNumber = int(
        input("---------------------\n1.구구단 출력\n2.프로그램 종료\n---------------------\n"))

# 메뉴에서 1선택시 구구단 출력,2인경우 msg 출력후 프로그램 종료
    if inputNumber == 1:
        multiply_Number = int(input("출력할 구구단의 단을 입력하세요.구구단의 단은 2~9사이 입력\n"))
    elif inputNumber == 2:
        print("이용해주셔서 감사합니다")
        break
# 메뉴에서 1또는 2 이외의 값이 입력될경우,Error Msg,출력후 재입력
    else:
        print("잘못입력하셨습니다.다시 입력하세요")
        continue

        # 구구단 출력 메뉴 선택시 출력할 단을 키보드로부터 입력 2~9
    if 1 < multiply_Number < 10:
        for number in range(1, 10):
            print(multiply_Number, "X", number, "=", multiply_Number*number)

# 2~9단 이외의 값이 들어온 경우 Error Msg출력후 재입력
    else:
        print("2~9사이의 정수를 입력해주세요.")
        continue
