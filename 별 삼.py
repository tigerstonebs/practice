num = 5
median = num//2+1

for row_num in range(num):
    # 증가 반복문 : ROW_NUM < median
    if row_num < median:
        for star_count in range(row_num+1):
            print("*", " ", end="")
    # 감소 반복문
    else:
        for star_count in range(num-row_num):
            print("*", " ", end="")
    print()
