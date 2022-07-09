# 실버1 https://www.acmicpc.net/problem/1446

N, D = map(int, input().split())
dp = [i for i in range(D + 1)]
shortcut = []

for _ in range(N):
    sc = list(map(int, input().split()))
    if sc[1] > D or (sc[2] >= (sc[1] - sc[0])):  # 쓰레기 지름길 처리
        continue
    shortcut.append(sc)
shortcut.sort(key=lambda x: x[0])

for i in range(D + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    for start, end, dis in shortcut:
        if i == start and dp[i] + dis < dp[end]:
            dp[end] = dp[i] + dis
print(dp[D])
