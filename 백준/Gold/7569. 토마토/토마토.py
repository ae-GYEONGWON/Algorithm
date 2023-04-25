import sys
from collections import deque
from itertools import chain
input = sys.stdin.readline

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0]*m for _ in range(n)] for _ in range(h)]
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
T = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                T.append((i, j, k))

visited = [[[0]*m for _ in range(n)] for _ in range(h)]
while T:
    i, j, k = T.popleft()
    for idx in range(6):
        nx = i + dx[idx]
        ny = j + dy[idx]
        nz = k + dz[idx]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
            if tomato[nx][ny][nz] == 0 and not visited[nx][ny][nz]:
                visited[nx][ny][nz] = 1
                tomato[nx][ny][nz] = tomato[i][j][k] + 1
                T.append((nx, ny, nz))
temp_tomato = []

for i in tomato:
    temp_tomato.extend(chain(*i))
if 0 in temp_tomato:
    print(-1)
else:
    print(max(temp_tomato)-1)

