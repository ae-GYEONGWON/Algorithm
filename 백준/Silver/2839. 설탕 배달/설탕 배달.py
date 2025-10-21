import sys

input = sys.stdin.readline

N = int(input())

dp = [-1]*4995
dp = [-1, -1, -1, 1, -1, 1] + dp

if N < 6:
    print(dp[N])
    exit(0)
    
for i in range(6, N+1):
    if dp[i-3] == -1 and dp[i-5] == -1:
        continue
    
    if dp[i-3] == -1:
        dp[i] = dp[i-5] + 1
        continue
    
    if dp[i-5] == -1:
        dp[i] = dp[i-3] + 1
        continue
    
    dp[i] = min(dp[i-3] + 1, dp[i-5] + 1)
    
        
print(dp[N])