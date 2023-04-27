import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
apt = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
answer = []
q = deque()
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1 and not visited[i][j]:
            q.append((i, j))
            visited[i][j] = 1
            cnt = 1
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            while q:
                x, y = q.popleft()
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0 <= xx < n and 0 <= yy < n:
                        if not visited[xx][yy] and apt[xx][yy] == 1:
                            visited[xx][yy] = 1
                            q.append((xx, yy))
                            cnt += 1
            answer.append(cnt)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
                            