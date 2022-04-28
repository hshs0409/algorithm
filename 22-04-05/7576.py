from collections import deque
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
M, N = map(int, input().split())
box = [0] * N
visited, day_count = [[False for _ in range(M)] for _ in range(N)], 0
q = deque()
for y in range(N):
    row = list(map(int, input().split()))
    box[y] = (row)
    for x in range(M):
        if row[x] == 1:
            q.append((y, x, day_count))
            visited[y][x] = True

while q:
    cy, cx, day = q.popleft()
    day_count = max(day, day_count)
    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]
        if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0 and visited[ny][nx] == False:
            box[ny][nx] = 1
            visited[ny][nx] = True
            q.append((ny, nx, day + 1))

ripe_flag = False
for y in range(N):
    for x in range(M):
        if box[y][x] in [-1, 1]:
            pass
        else:
            ripe_flag = True
print(day_count) if not ripe_flag else print('-1')
