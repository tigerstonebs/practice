# 키보드로부터 line수 를 입력 받는다.
from tkinter import Y
n = 0  # 인덱스
value = str()  # 리스트에 넣기전에 원소들이 있는 공간
my_list = []
real_list = []

a = input("입력 문자열의 줄(line)수를 입력하세요.")

# 라인의 문자열을 입력
for val in range(int(a)):
    my_list = list(input(str(val+1)+"번째 라인의 문자열을 입력하세요."))


for i in my_list:
    n += 1
    if i == ' ':
        real_list.append(value)
        value = str()
    elif n == len(my_list):
        value += i
        real_list.append(value)
    else:
        value += i
n = 0


# 검색할 문자를 입력 받는다
while True:
    search_list = []
    research_list = []
    search_list = list(input("검색 할 문자열을 입력하세요."))

    v = str()
    for i in search_list:
        n += 1
        if n == len(search_list):
            v += i
            research_list.append(v)
        else:
            v += i
    n = 0

    # 총단어수 검색된횟수 검색된라인수 구하기
    # 검색된 횟수
    count = len(real_list)
    line = 0
    word = 0
    line_va = 0
    for va in real_list:
        if va in research_list:
            word += 1
            line_va = real_list.index(va)
            print(str(research_list)+"를 찾았습니다.")
            print("총 단어 수:"+str(count))
            print("검색된 라인수:"+str(line_va+1))
            print("검색된 횟수:"+str(word))
            break

        else:
            print("찾을수가 없습니다.")
            continue
