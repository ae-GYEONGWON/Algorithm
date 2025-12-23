import sys
from collections import deque

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    new_q: deque = deque()
    for i in range(len(q)):
        new_q.append((i, q[i]))
    max_num = max(q)

    cnt = 0
    while new_q:
        idx, num = new_q.popleft()
        _num = q.popleft()
        if num < max_num:
            new_q.append((idx, num))
            q.append(_num)
        else:
            cnt += 1
            if not q:
                print(cnt)
                break
            max_num = max(q)

            if idx == m:
                print(cnt)
                break
    
