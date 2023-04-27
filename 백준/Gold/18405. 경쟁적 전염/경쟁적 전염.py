import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
examiner = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
q = []
for i in range(n):
    for j in range(n):
        if examiner[i][j] != 0:
            q.append((examiner[i][j], i, j))
q.sort()
q = deque(q)
du = [1, -1, 0, 0]
dv = [0, 0, 1, -1]
for _ in range(s):
    for _ in range(len(q)):
        virus, u, v = q.popleft()
        for i in range(4):
            nu = u + du[i]
            nv = v + dv[i]
            if 0 <= nu < n and 0 <= nv < n:
                if examiner[nu][nv] == 0:
                    examiner[nu][nv] = virus
                    q.append((virus, nu, nv))


print(examiner[x-1][y-1])