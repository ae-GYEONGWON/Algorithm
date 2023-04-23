import sys
input = sys.stdin.readline

n = int(input())
status = '0'+input().rstrip()
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
cnt = 0

def dfs(x):
    global cnt
    for i in graph[x]:
        if not visited[i]:
            if status[i] == '1':
                cnt += 1
                visited[i] = 1
            else:
                visited[i] = 1
                dfs(i)
                visited[i] = 0
            
for i in range(1, n+1):
    visited = [0]*(n+1)
    visited[i] = 1
    if status[i] == '1':
        dfs(i)

print(cnt)