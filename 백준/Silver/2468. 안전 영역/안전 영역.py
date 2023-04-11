from collections import deque

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
ans = 0
max_height = 0
for i in map:
    temp_max = max(i)
    if temp_max > max_height:
        max_height = temp_max

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for height in range(max_height):
    visited = [[0]*n for _ in range(n)]
    safe_area = 0
    for i in range(n):
        for j in range(n):
            if map[i][j] > height and visited[i][j] == 0:
                q = deque()
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < n and 0 <= yy < n:
                            if visited[yy][xx] == 0 and map[yy][xx] > height:
                                q.append([yy, xx])
                                visited[yy][xx] = 1
                safe_area += 1
    
    if safe_area > ans:
        ans = safe_area
print(ans)