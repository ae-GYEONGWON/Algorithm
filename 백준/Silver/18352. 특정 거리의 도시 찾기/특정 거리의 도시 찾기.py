import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
answer_list = [1]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append(x)
visited[x] = 1
while q:
    now = q.popleft()
    for next in graph[now]:
        if not visited[next]:
            visited[next] = 1
            q.append(next)
            answer_list[next] += answer_list[now]



for i in range(1, len(answer_list)):
    if i == x: continue
    if answer_list[i]-1 == k:
        print(i)

answer_list = answer_list[1:x]+answer_list[x+1:]
if not k+1 in answer_list:
    print(-1)