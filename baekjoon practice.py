# a = int(input())
# if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
#     print(1)
# else:
#     print(0)
# a = int(input())
# b = int(input())

# if a > 0 and b > 0:
#     print(1)
# elif a < 0 and b > 0:
#     print(2)
# elif a < 0 and b < 0:
#     print(3)
# elif a > 0 and b < 0:
#     print(4)
# H, M = map(int, input().split())
# if M > 44:
#     print(H, M-45)
# elif M < 45 and H > 0:
#     print(H-1, M+15)
# else:
#     print(23, M+15)
# H, M = map(int, input().split())
# timer = int(input())

# H += timer // 60
# M += timer % 60

# if M >= 60:
#     H += 1
#     M -= 60
# if H >= 24:
#     H -= 24

# print(H,M)
# a, b, c = map(int, input().split())

# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# else:
#     print(100 * max(a,b,c))
