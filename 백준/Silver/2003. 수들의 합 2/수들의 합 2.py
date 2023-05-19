import sys
from itertools import accumulate
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
start = 0
while start < n:
    temp = start
    sum_num = A[temp]
    while (temp+1) < n and (sum_num + A[temp+1]) <= m:
        temp += 1
        sum_num += A[temp]

    if sum_num == m:
        ans += 1
    start += 1

print(ans)