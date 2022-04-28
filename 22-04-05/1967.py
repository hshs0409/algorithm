import math
import heapq
import sys
input = sys.stdin.readline
INF, result = math.inf, 0
N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a, b, r = map(int, input().split())
    graph[a].append((b, r))
    graph[b].append((a, r))


def dijkstra(start):
    global result
    q = []
    distance = [INF] * (N + 1)
    distance[0], distance[start] = 0, 0
    heapq.heappush(q, (start, distance[start]))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
    for idx, val in enumerate(distance):
        if val == INF:
            distance[idx] = 0
    last_idx = sorted(
        range(len(distance)), key=lambda i: distance[i], reverse=True)[0]
    result = distance[last_idx]
    return last_idx


dijkstra(dijkstra(1))
print(result)
