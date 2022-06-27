from collections import deque


def bfs():
    dq = deque()
    dq.append((home_y, home_x))
    visit_set = set()
    visit_set.add((home_y, home_x))
    while dq:
        cur_y, cur_x = dq.popleft()
        if abs(cur_y - fest_y) + abs(cur_x - fest_x) <= 1000:
            print('happy')
            return

        for con_y, con_x in convs:
            if (con_y, con_x) not in visit_set:
                if abs(con_y - cur_y) + abs(con_x - cur_x) <= 1000:
                    dq.append((con_y, con_x))
                    visit_set.add((con_y, con_x))
    print('sad')


for _ in range(int(input())):
    N = int(input())  # 편의점 개수
    home_y, home_x = map(int, input().split())
    convs = []
    for _ in range(N):
        con_y, con_x = map(int, input().split())
        convs.append((con_y, con_x))
    fest_y, fest_x = map(int, input().split())
    bfs()
