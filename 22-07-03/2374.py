# 같은 수로 만들기 골드 4 https://www.acmicpc.net/problem/2374

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
prev = int(input())
max_num = prev
for _ in range(N - 1):
    curr = int(input())
    if prev < curr:
        cnt += curr - prev
        max_num = max(max_num, curr)
    prev = curr
cnt += max_num - prev
print(cnt)
