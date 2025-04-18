import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

visited = [False for _ in range(100001)]
q = deque()
q.append([N, 0])
visited[N] = True

while q:
    num, cnt = q.popleft()

    if num == K:
        print(cnt)
        break

    for n_num in [num + 1, num - 1, num * 2]:
        if 0 <= n_num <= 100000 and not visited[n_num]:
            visited[n_num] = True
            q.append([n_num, cnt + 1])
