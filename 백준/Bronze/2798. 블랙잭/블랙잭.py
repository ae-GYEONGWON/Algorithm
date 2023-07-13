import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

combi = list(combinations(nums, 3))

ans = 0
for i in combi:
    temp = sum(i)
    if temp <= m and ans < temp:
        ans = temp
    
print(ans)