import sys
import math
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0]+[math.inf]*k

for coin in coins:
    for i in range(1, k+1):
        if i-coin >= 0:
            dp[i] = min(dp[i-coin]+1, dp[i])

if dp[-1] == math.inf:
    print(-1)
else:
    print(dp[-1])