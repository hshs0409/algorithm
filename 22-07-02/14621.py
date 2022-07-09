# 골드3 나만 안되는 연애 https://www.acmicpc.net/problem/14621

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
school_list = list(map(str, input().split()))
school_check = [1 if school == "M" else 0 for school in school_list]
parent = [i for i in range(N + 1)]

graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x: x[2])
result, count = 0, 0
for a, b, cost in graph:
    if school_check[a - 1] + school_check[b - 1] == 1:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            count += 1

print(result) if N - 1 == count else print(-1)
