from collections import deque

N, M = map(int, input().split())
computers = [[] for _ in range(N)]
result = [0] * (N)  ## 정답 배열

for i in range(M):
    a, b = map(int, input().split())
    computers[b - 1].append(a - 1)


def bfs(start):
    visited = [False] * N
    visited[start] = True
    q = deque()
    q.append(start)
    cnt = 1  ## 현재 번호에서 해킹할 수 있는 컴퓨터 개수
    while q:
        now = q.popleft()
        for next in computers[now]: ## 다음으로 방문할 수 있는 곳
            if visited[next] == False: ## 방문하지 않은 곳일 때
                q.append(next)
                visited[next] = True
                cnt += 1
    return cnt ## 개수 리턴

for i in range(N):
    result[i] = bfs(i)
max_result = max(result)

for idx, val in enumerate(result):
    if val == max_result:
        print(idx + 1, end=" ")