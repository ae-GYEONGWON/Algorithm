import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, color):
    global answer
    
    for i in graph[start]:
        if not visited[i]:
            visited[i] = -color
            dfs(i, -color)
        elif visited[i] == -color:
            pass
        else:
            answer = "NO"
            break

k = int(input())
for _ in range(k):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    answer = "YES"
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V):
        if not visited[i]:
            dfs(i, 1)
    print(answer)