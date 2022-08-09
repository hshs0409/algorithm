# 별 찍기 - 1 브론즈 5 https://www.acmicpc.net/problem/2438

N = int(input())
stars = []
for i in range(N):
    print(' ' * i + '*' * (2 * (N - i) - 1))
    if i != N - 1:
        stars.append(' ' * i + '*' * (2 * (N - i) - 1))
for star in reversed(stars):
    print(star)
