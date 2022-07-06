count = 1
while True:
    number = int(input("정수를 입력해주세요"))
    if number == 20000:
        print("이용해주셔서 감사합니다.")
        break
    if number > 0:
        if number == 1:
            print("{}번째 입력값은 ={} \n\t\t 홀수입니다.".format(count, number))
            count += 1
        elif number % 3 == 0:
            print("{}번째 입력값은 ={} \n\t\t 홀수입니다.\n\t\t3의배수입니다.".format(count, number))
            count += 1
        elif number % 7 == 0:
            print("{}번째 입력값은 ={} \n\t\t 홀수입니다.\n\t\t7의배수입니다.".format(count, number))
            count += 1
        elif number % 2 == 0:
            print("{}번째 입력값은 ={} \n\t\t 짝수입니다.".format(count, number))
            count += 1
        elif number % 1 == 0:
            print("{}번째 입력값은 ={} \n 홀수입니다.".format(count, number))
            count += 1
    if number <= 0:
        print("1이상 양수를 입력해주십시오.")
