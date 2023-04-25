import sys
from collections import deque
import itertools

input = sys.stdin.readline

T = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
# print(M, N)
# print(graph)
# print(temp)
for j in range(N):
    for i in range(M):
        if graph[j][i] == 1:
            T.append((i, j))
# print(T)
while T:
    x, y = T.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                T.append((nx, ny))

graph2 = list(itertools.chain(*graph))
if 0 in graph2:
    ans = -1
else :
    ans = max(graph2) - 1
# print(temp)
# print(graph)
print(ans)