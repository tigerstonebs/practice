
from email.mime import base
import random
from zlib import DEFLATED
# 0~9사이의 랜덤 숫자중 중복되지 않은 3개의 숫자를 랜덤으로 출력
mylist = []
for i in range(3):
    val = random.randint(0, 9)
    while val in mylist:
        val = random.randint(0, 9)
    mylist.append(val)
print(mylist)

# 키보드로부터 0~9사이의 정수3개를 입력받고 결과값 출력
시도횟수 = 1
strikeout = 0
while True:
    print("시도횟수:"+str(시도횟수))
    baselist = []
    for value in range(3):
        baselist.append(int(input("정수를 입력하세요")))
    print(baselist)
    시도횟수 += 1
    # 스트라이크,볼이 생기는 경우
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if baselist[i] == mylist[i]:
            strike_count += 1
            if strike_count == 3:
                break
        elif baselist[i] in mylist and baselist[i] != mylist[i]:
            ball_count += 1
    # 스트라이크.볼 출력
    if strike_count > 0:
        print(strike_count, "strike")
    if ball_count > 0:
        print(ball_count, "ball")

    # out이 생기는경우
    if baselist[0] not in mylist and baselist[1] not in mylist and baselist[2] not in mylist:
        strikeout += 1
    if strikeout > 0:
        print("Out:아웃", strikeout, "번")
    # 패배 하게되는 경우
    if strikeout == 2 or 시도횟수 > 5:
        print("패배\n정답은", str(mylist))
        break
    # 승리하게 되는 경우
    if strike_count == 3:
        print("패배\n정답은", str(mylist))
        break
