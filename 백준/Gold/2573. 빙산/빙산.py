import sys
from collections import deque
# sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
time = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 빙판 갯수 세는 함수
def cnt_mnt(graph):
    global n, m
    visited = [[0]*m for _ in range(n)]
    q = deque()
    cnt = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j] and not visited[i][j]:
                visited[i][j] = 1
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 < xx < n and 0 < yy < m:
                            if graph[xx][yy] and not visited[xx][yy]:
                                visited[xx][yy] = 1
                                q.append((xx, yy))
                cnt += 1
    return cnt

# 일년 뒤 빙산을 만드는 함수
def make_next_graph(graph):
    global n, m
    next_graph = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            cnt = 0
            if graph[i][j] and not visited[i][j]:
                visited[i][j] = 1
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < m:
                        if graph[x][y] == 0:
                            cnt += 1
                
                next_graph[i][j] = max(graph[i][j] - cnt, 0)
    return next_graph

# 종료 조건이 맞을 때까지 재귀하는 함수
def sol(graph):
    global time
    
    sum_mnt = 0
    for i in range(1, n-1):
        sum_mnt += sum(graph[i])
    if sum_mnt == 0:
        time = 0
        return 
    if cnt_mnt(graph) > 1:
        return 

    graph = make_next_graph(graph)
    time += 1
    sol(graph)

sol(graph)
print(time)