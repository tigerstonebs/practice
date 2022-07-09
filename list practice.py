# 1~20 사이 양의 정수 중 난수 값 20개를 생성후 list에 저장
# 랜덤 함수 불러오기
import random
from re import L
from stringprep import map_table_b2
from token import PLUSEQUAL
# 리스트 만들기
myList = []
# 20번 반복
for value in range(20):
    # 리스트에 1~20사이의 난수를 저장
    myList.append(random.randint(1, 20))
print(("랜덤 값 :\n")+str(myList))

# List 내 원소 값에 대한 합계,평균,최대값,최소값 출력
# 합계
plus = 0
for i in myList:
    plus += i
print(("합계\t:")+str(plus))

# 평균
a = (plus/20)
print(("평균\t:")+str(a))

# 최댓값
maximum = myList[0]
for i in myList:
    if i > maximum:
        maximum = i
print(("최댓값  :")+str(maximum))
# 최솟값
minimum = myList[0]
for i in myList:
    if i < minimum:
        minimum = i
print(("최솟값  :")+str(minimum))

# 중복값 출력
first_index = []
twin_index = []

for val in myList:
    if val not in first_index:  # 처음 등장한 원소
        first_index.append(val)

    else:
        if val not in twin_index:  # 이미 중복 원소로 판정된 경우는 제외
            twin_index.append(val)


# 중복값 개수 구하기
print("중복값\t중복횟수")
j = 0
for j in range(len(twin_index)):  # 중복원소 리스트에 인덱스 개수 세기
    a = 0
    for i in range(len(myList)):  # 리스트에 있는 인덱스 개수 세기
        if twin_index[j] == myList[i]:
            a += 1
    c = print(twin_index[j], a, sep='\t')


# 구간별 히스토그램 만들기
# 1~5사이의 원소의 개수 구하기
print("구간별 히스토그램")
star_one = 0
for hit in range(20):  # hit=0~19
    if 0 < myList[hit] < 6:  # 리스트 전체를 돌면서 1~5사이의 수를 서치
        star_one += 1       # 찾았다면 변수에 1을 더하기
print(str("1 ~ 5 :")+("*" * star_one))
# 6~10사이의 원소의 개수 구하기
star_two = 0
for hit in range(20):  # hit=0~19
    if 5 < myList[hit] < 11:  # 리스트 전체를 돌면서 1~5사이의 수를 서치
        star_two += 1       # 찾았다면 변수에 1을 더하기
print(str("6 ~ 10 :")+("*" * star_two))
# 11~15사이의 원소의 개수 구하기
star_thr = 0
for hit in range(20):  # hit=0~19
    if 10 < myList[hit] < 16:  # 리스트 전체를 돌면서 1~5사이의 수를 서치
        star_thr += 1       # 찾았다면 변수에 1을 더하기
print(str("11 ~ 15 :")+("*" * star_thr))
# 16~20사이의 원소의 개수 구하기
star_four = 0
for hit in range(20):  # hit=0~19
    if 15 < myList[hit] < 21:  # 리스트 전체를 돌면서 1~5사이의 수를 서치
        star_four += 1       # 찾았다면 변수에 1을 더하기
print(str("16 ~ 20 :")+("*" * star_four))
