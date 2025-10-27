import sys
from collections import deque

input = sys.stdin.readline
    
        
while True:
    w, h = map(int, input().split())
    
    if all(num == 0 for num in (w, h)):
        break
    
    graph = []
    cnt = 0
    for _ in range(h):
        g = list(map(int, input().split()))
        graph.append(g)
        
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                dx = [0, 1, 0, -1, 1, 1, -1, -1]
                dy = [1, 0, -1, 0, 1, -1, 1, -1]
                while q:
                    y, x = q.popleft()
                    
                    for idx in range(8):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
                            if graph[ny][nx] == 1:
                                visited[ny][nx] = True
                                q.append((ny, nx))
                cnt += 1
    print(cnt)
