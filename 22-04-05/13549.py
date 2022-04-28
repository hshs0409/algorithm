from collections import deque

N, K = map(int, input().split())
max_dist = 100001
visited = [False] * max_dist

def bfs(cur, time):
    q = deque()
    q.append((cur, time))
    visited[cur] = True
    while q:
        cur, time = q.popleft()
        visited[cur] = True
        if cur == K:
            return time

        for next in [cur * 2, cur + 1, cur - 1]:
            if 0 <= next <= max_dist - 1 and visited[next] == False:
                q.appendleft((next, time)) if next == cur * 2 else q.append((next, time + 1))

print(bfs(N, 0))
