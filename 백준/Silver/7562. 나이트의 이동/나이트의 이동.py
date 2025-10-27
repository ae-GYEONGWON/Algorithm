import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    I = int(input())
    now = tuple(map(int, input().split()))
    to_go = tuple(map(int, input().split()))
    
    visited = [[False]*I for _ in range(I)]
    q = deque()
    start_point = (now[0], now[1], 0)
    q.append(start_point)
    dx = [1, -1, 1, -1, 2, 2, -2, -2]
    dy = [2, 2, -2, -2, 1, -1, 1, -1]
    while q:
        x, y, point = q.popleft()
        
        if x == to_go[0] and y == to_go[1]:
            print(point)
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and not visited[ny][nx]:
                visited[ny][nx] = True
                new_point = point + 1
                q.append((nx, ny, new_point))