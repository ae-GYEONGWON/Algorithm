import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1


def bfs(a):
    visited = [0]*len(graph)
    q = deque()
    q.append(a)
    visited[a] = 1
    print(a, end=" ")
    while q:
        x = q.popleft()
        for i in range(1, len(graph[x])):
            if graph[x][i] != 0:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    print(i, end=" ")


def dfs(a):
    visited[a] = 1
    print(a,end =" ")

    for i in range(len(graph[a])):
        if graph[a][i] == 1 and visited[i] == 0:
            dfs(i)



visited = [0]*len(graph)
dfs(v)
print()
bfs(v)