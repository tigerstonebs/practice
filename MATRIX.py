import random
matrix_list = []
line = []
# 난수 리스트 만들기

while len(line) < 5:
    num = random.randint(1, 50)
    if num not in line:
        line.append(num)
        matrix_list.append(line)
print(matrix_list)


# # 열에 따라서 나온는 결과값
# 최소값
minimum = matrix_list[0]
for i in matrix_list[:4]:
    if i < minimum:
        minimum = i

print(("최솟값  :")+str(minimum))
