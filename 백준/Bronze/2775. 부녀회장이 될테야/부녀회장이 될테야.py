import sys
input = sys.stdin.readline

dp = [[0]*15 for _ in range(15)]
for i in range(15):
    dp[0][i] = i
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    if k == 0:
        print(dp[k][n])
        continue
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = sum(dp[i-1][:j+1])
    print(dp[k][n])