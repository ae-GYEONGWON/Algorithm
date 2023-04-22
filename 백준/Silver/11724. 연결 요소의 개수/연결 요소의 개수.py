import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]
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

for xx, yy in data:
    union(xx, yy)

for i in range(len(parent)):
    find(i)
print(len(set(parent[1:])))