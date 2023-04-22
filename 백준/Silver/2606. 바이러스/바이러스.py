from collections import deque

N = int(input())
link = int(input())

network = [[] * (N + 1) for _ in range(N + 1)]

for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited = [0] * (N + 1)
cnt = 0

def bfs (virus):
    global cnt
    visited[virus] = 1
    q = deque([virus])
    while q:
        for i in network[q.popleft()]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                cnt += 1
    return cnt
    
print(bfs(1))