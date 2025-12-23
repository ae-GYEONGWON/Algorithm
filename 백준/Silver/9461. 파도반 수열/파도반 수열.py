import sys

input = sys.stdin.readline

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*90

"""
dp[11] = 12 = 9 + 3 = dp[10] + dp[6]
dp[12] = 16 = 12 + 4 = dp[11] + dp[7]
dp[13] = 21 = 16 + 5 = dp[12] + dp[8]
...
dp[n] = dp[n-1] + dp[n-5]
"""

t = int(input())
for _ in range(t):
    n = int(input())
    if n < 11:
        print(dp[n])
    else:
        for i in range(10, n+1):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[n])
