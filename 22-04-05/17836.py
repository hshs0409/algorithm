from collections import deque

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]

result = T + 1
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[False for _ in range(M)] for _ in range(N)]

q = deque()
q.append((0, 0, 0))
while q:
    y, x, t = q.popleft()
    if x + y == N + M - 2:
        result = min(result, t)
        break
    if t > T:
        break
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False:
            if castle[ny][nx] == 0:
                q.append((ny, nx, t + 1))
                visited[ny][nx] = True
            elif castle[ny][nx] == 1:
                continue
            else:
                visited[ny][nx], short_dis = True, t + 1 + (N + M - 2) - (ny + nx)
                result = min(result, short_dis)
                q.append((M, N, short_dis))

print(result) if result <= T else print("Fail")