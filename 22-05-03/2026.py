# 소풍
import sys
input = sys.stdin.readline
K, N, F = map(int, input().split())
friends_list = [[] for _ in range(N + 1)]
for _ in range(F):  # 인접 리스트 생성
    one, two = map(int, input().split())
    friends_list[one].append(two)
    friends_list[two].append(one)


def dfs(idx, friends):
    if len(friends) == K:  # 작은 것부터 시작하기에 바로 나온놈이 정답
        for friend in friends:
            print(friend)
        exit()
    for i in range(idx + 1, N + 1):
        if visited[i] == False:  # 각 친구별로 관계 뒤져보기
            for friend in friends:
                if friend not in friends_list[i]:
                    break
            else:
                visited[i] = True
                dfs(idx, friends + [i])


for i in range(1, N+1):
    visited = [False]*(N + 1)
    visited[i] = True
    dfs(i, [i])

print(-1)
