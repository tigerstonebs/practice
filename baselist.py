# 사용자가 번호를 등록
#mysrtring = (input("주민등록번호를 입력해주세요."))


mysrtring = "000712-3184923"
# 각 번호마다 체크수를 곱하기
val = 2
j = 0
mylist = []
a = 0
# 체크수를 번호마다 곱하기
value = 0
for va in mysrtring[:-1]:
    if va.isdigit():
        value = val*int(va)
        val += 1
        if val >= 10:
            val = 2
        mylist.append(value)

# 나온 결과를 더하기
plus = 0
for i in mylist:
    plus += i

# 체크계산 하기
value = (11-(plus % 11))
if value == int(mysrtring[-1]) or value % 10 == int(mysrtring[-1]):
    print("유효한 주민번호 입니다.")
else:
    print("유효하지않은 주민번호입니다.")
