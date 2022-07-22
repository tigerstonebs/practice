b = 0
for i in range(5):
    a = (int(input(str(i+1)+"번째 값 입력")))
    b += a
print("합계:"+str(b))
print("평균:"+str(b/5))

while True:
    val = int(input("정수를 입력하세요"))
    if val > 0:
        print("양수입니다.")
    elif val < 0:
        print("음수입니다.")
    else:
        break

c = 5
for i in range(c):
    for del_val in range(i+2):
        print(" ", end="")
    for j in range(c-i):
        print("*", end="")
    print()


for i in range(1, 100):
    s = str(i)
    count = 0
    for x in s:
        if x == '3':
            count += 1
    if count == 0:
        print('', end="")
    else:
        print(i)

myList = "!! hello world, it is awesome day."
print("특수문자 수:"+str(myList.count("!")+myList.count(".")+myList.count(",")))
a = len(myList.split(' '))
b = str(a-1)
print("단어 수:"+b)

c = (len(myList))
print("단어수:"+str(c-a-3))
