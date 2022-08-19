# [BOJ} 16507 어두운 건 무서워 /실버 1 https://www.acmicpc.net/problem/16507

import sys
input = sys.stdin.readline
R, C, Q = map(int, input().split())

photos = [list(map(int, input().split())) for _ in range(R)]
parts = [list(map(int, input().split())) for _ in range(Q)]

p_sums = [[[] for _ in range(C+1)] for _ in range(R)]
for r, photo in enumerate(photos):
    temp_sum = 0
    p_sums[r][0] = 0
    for c, p in enumerate(photo):
        temp_sum += p
        p_sums[r][c+1] = temp_sum

for r1, c1, r2, c2 in parts:
    avg = 0
    for r in range(r1 - 1, r2):
        avg += p_sums[r][c2] - p_sums[r][c1-1]

    if r1 == r2:
        if c1 == c2:
            print(photos[r1-1][c1-1])
            continue
        print((p_sums[r2-1][c2] - p_sums[r1-1][c1-1]) // (c2 - c1 + 1))
    else:
        print(avg // ((r2 - r1 + 1) * (c2 - c1 + 1)))
