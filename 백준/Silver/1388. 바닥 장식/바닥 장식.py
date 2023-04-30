import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
badak = [list(input().rstrip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
d = [1, -1]
def bfs(a, b):
    next_visit_q = deque()
    next_visit_q.append((a, b))
    visited[a][b] = 1
    if badak[a][b] == "-":
        while next_visit_q:
            x, y = next_visit_q.popleft()
            for i in range(2):
                ny = y + d[i]
                if 0 <= ny < m:
                    if not visited[x][ny] and badak[x][ny] == "-":
                        visited[x][ny] = 1
                        next_visit_q.append((x, ny))
    else:
        while next_visit_q:
            x, y = next_visit_q.popleft()
            for i in range(2):
                nx = x + d[i]
                if 0 <= nx < n:
                    if not visited[nx][y] and badak[nx][y] == "|":
                        visited[nx][y] = 1
                        next_visit_q.append((nx, y))
ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs(i, j)
            ans += 1

print(ans)