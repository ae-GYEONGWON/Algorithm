import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heavier = dict()
lighter = dict()
res = 0
#  지렸다.
for _ in range(m):
    a, b = map(int, input().split())
    if b in heavier:
        heavier[b].append(a)
    else:
        heavier[b] = [a]

    if a in lighter:
        lighter[a].append(b)
    else:
        lighter[a] = [b]


def dfs(x: int, y: dict):
    visited[x] = True
    if x in y:
        for i in y[x]:
            if not visited[i]:
                visited[i] = True
                dfs(i, y)

for i in heavier:
    visited = [False]*(n+1)
    dfs(i, heavier)
    if visited.count(True)-1 >= (n+1)//2:
        res += 1
for i in lighter.keys():
    visited = [False]*(n+1)
    dfs(i, lighter)
    if visited.count(True)-1 >= (n+1)//2:
        res += 1
print(res)
