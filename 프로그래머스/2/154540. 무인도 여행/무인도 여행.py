from collections import deque

def solution(maps):
    answer = []
    
    # bfs를 돌면서 섬을 찾아서 값을 aswer에 넣는다
    # 모두 방문한 이후에 answer가 비었으면 -1을 반환.
    # 그렇지 않으면 오름차순으로 정렬해서 반환.
    
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    ways = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    def bfs(s_point):
        res = int(maps[s_point[1]][s_point[0]])
        q = deque()
        q.append(s_point)
        visited[s_point[1]][s_point[0]] = True
        while q:
            x, y = q.popleft()
            for way in ways:
                nx = x + way[0]
                ny = y + way[1]
                if 0 <= nx < cols and 0 <= ny < rows and not visited[ny][nx] and maps[ny][nx] != "X":
                    visited[ny][nx] = True
                    q.append((nx, ny))
                    res += int(maps[ny][nx])
        return res
    
    for row in range(rows):
        for col in range(cols):
            if not visited[row][col] and maps[row][col] != "X":
                answer.append(bfs((col, row)))
    
    answer = sorted(answer) if answer else [-1]
    return answer
