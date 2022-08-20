# [BOJ] 20159 동작 그만, 밑장 빼기냐? / 골드 5 https://www.acmicpc.net/problem/20159

import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
left_sum, right_sum, left_prefix, right_prefix = [0], [0], 0, 0
for left, right in zip(cards[::2], cards[1::2]):
    left_prefix += left
    right_prefix += right
    left_sum.append(left_prefix)
    right_sum.append(right_prefix)

_max = left_sum[-1]

for i in range(N//2):
    _left_temp_sum = (left_sum[i]) + (right_sum[-1] - right_sum[i])
    _right_temp_sum = (left_sum[i+1]) + (right_sum[-2] - right_sum[i])
    _max = max(_left_temp_sum, _max)
    _max = max(_right_temp_sum, _max)

print(_max)
