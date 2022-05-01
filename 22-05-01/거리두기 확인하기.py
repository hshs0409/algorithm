def solution(places):
    answer = [1] * len(places)
    dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]

    for place_idx, place in enumerate(places):
        participants, tables = [], []
        for y in range(5):
            for x in range(5):
                if place[y][x] == "P":
                    participants.append((y, x))
                elif place[y][x] == "O":
                    tables.append((y, x))
                    
        ## 응시자 주변 확인
        for py, px in participants:
            for i in range(4):
                ny, nx = py + dy[i], px + dx[i]
                if 0 <= ny < 5 and 0 <= nx < 5 and place[ny][nx] == "P":
                    answer[place_idx] = 0
                    
        ## 빈 테이블 주변 확인
        for ty, tx in tables:
            p_count = 0
            for i in range(4):
                ny, nx = ty + dy[i], tx + dx[i]
                if 0 <= ny < 5 and 0 <= nx < 5 and place[ny][nx] == "P":
                    p_count += 1
                if p_count >= 2:
                    answer[place_idx] = 0

    return answer