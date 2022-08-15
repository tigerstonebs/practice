import random
from re import A
from secrets import choice

# 리스트 선언
word_List = []
# 키보드로부터 영어 단어 3개를 입력받아 리스트에 저장
while len(word_List) < 3:
    word = input(str(len(word_List)+1)+"번째 단어를 입력하세요.")
    if 20 >= len(word) >= 5:
        word_List.append(word)

    else:
        word = input("5이상 20이하 글자로 구성된 단어를 입력하세요.")
        word_List.append(word)
# 입력된 3개의 단어 중 한 개 단어를 임의 선택
choicelist = random.choice(word_List)
choicelist = "samsung"
print("단어 선택완료 게임을 시작합니다.선택된단어:"+choicelist)
# 선택된 단어의 글자 50%를 블라인드처리
blind = len(choicelist)/2

# 반올림


def roundUp(blind):
    if (blind - int(blind)) >= 0.5:
        return int(blind) + 1
    else:
        int(blind)


# 무작위로 글자 고르기

anwser = random.sample(choicelist, roundUp(blind))
print(anwser)


dictionary = {anwser[0]: "_", anwser[1]: "_", anwser[2]: "_", anwser[3]: "_"}
transTable = choicelist.maketrans(dictionary)
txt = choicelist.translate(transTable)
print(txt)


# 게임시작
a = input("1번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력하세요")
print(txt)
for a in choicelist:
    if a in txt:
        print()
