# https://www.acmicpc.net/problem/11052 실1

N = int(input())
cards = list(map(int, input().split()))

dp = [0] * (N + 1)
dp[1] = cards[0]

for i in range(2, N + 1):
    for j in range(1, N + 1):
        # dp[j] + dp[i - j] = j장 살때, i - j장 살때 최대 금액
        # cards[i-1] = 한 번에 살 때 카드 가격
        # dp[i] == 카드 i개 살 때 최대 금액
        print(dp[j] + dp[i - j], cards[i - 1], dp[i])
        dp[i] = max(dp[j] + dp[i - j], cards[i - 1], dp[i])

print(dp[-1])
