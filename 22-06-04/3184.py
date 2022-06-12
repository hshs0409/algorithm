
def dfs(y, x, flag):
    global result_sheep, result_wolf
    wolf = 1 if flag else 0
    sheep = 1 if not flag else 0
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        for i in range(4):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= ny < R and 0 <= nx < C and visited[ny][nx] != True and backyard[ny][nx] != "#":
                visited[ny][nx] = True
                if backyard[ny][nx] == "o":
                    sheep += 1
                elif backyard[ny][nx] == "v":
                    wolf += 1
                stack.append((ny, nx))
    if sheep > wolf:
        result_sheep += sheep
    else:
        result_wolf += wolf


R, C = map(int, input().split())
backyard = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
result_sheep, result_wolf = 0, 0

for y in range(R):
    for x in range(C):
        if backyard[y][x] in ["#", "."] and visited[y][x] == True:
            continue
        elif backyard[y][x] == "v" and visited[y][x] == False:
            visited[y][x] = True
            dfs(y, x, True)
        elif backyard[y][x] == "o" and visited[y][x] == False:
            visited[y][x] = True
            dfs(y, x, False)

print(result_sheep, result_wolf)
