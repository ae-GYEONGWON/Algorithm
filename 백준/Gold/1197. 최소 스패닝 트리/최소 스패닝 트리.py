import sys
input = sys.stdin.readline

v, e = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(e)]
data.sort(key = lambda x : x[2])
ans = 0
parent = [i for i in range(v+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b):
    A = find(a)
    B = find(b)
    if A > B:
        parent[A] = B
    else:
        parent[B] = A

for a, b, c in data:
    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)