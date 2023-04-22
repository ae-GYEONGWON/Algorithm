import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0]*(n+1)
ans = 0
def dfs(x):
    global ans
    visited[x] = 1
    for i in range(len(graph[x])):
        if graph[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            ans += 1
            dfs(i)
    return ans

print(dfs(1))
