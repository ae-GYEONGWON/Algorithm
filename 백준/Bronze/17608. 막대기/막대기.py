import sys
input = sys.stdin.readline
n = int(input())
h = [int(input()) for _ in range(n)]

cnt = 0; max_h = 0
for i in range(n-1,-1,-1):
    if h[i] > max_h:
        max_h = h[i]
        cnt += 1

print(cnt)