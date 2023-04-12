from collections import deque

def solution(maps):
    answer = 0
    m = len(maps[0])
    n = len(maps)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((0,0))
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            x = xx + dx[i]
            y = yy + dy[i]
            if 0 <= x < m and 0 <= y < n:
                if maps[y][x] == 1 and visited[y][x] == 0:
                    visited[y][x] = 1
                    maps[y][x] += maps[yy][xx]
                    q.append((x, y))
    # print(maps)
    # print(visited)
    if visited[n-1][m-1] == 0:
        return -1
    else :
        return maps[n-1][m-1]