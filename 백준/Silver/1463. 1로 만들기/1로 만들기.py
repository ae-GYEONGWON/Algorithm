import sys
import math

input = sys.stdin.readline

n = int(input().strip())

dp = [0, 0, 1, 1] + [math.inf]*(n-3)

if n < 4:
    print(dp[n])
else:
    for n in range(4, n+1):
        if n % 3 == 0:
            dp[n] = dp[n//3] + 1
        if n % 2 == 0:
            dp[n] = min(dp[n//2] + 1, dp[n])
        dp[n] = min(dp[n-1] + 1, dp[n])
    
    print(dp[n])