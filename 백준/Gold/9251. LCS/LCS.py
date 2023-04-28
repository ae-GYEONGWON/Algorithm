import sys
input = sys.stdin.readline

A1 = input().rstrip()
A2 = input().rstrip()

dp = [[0]*(len(A2)+1) for _ in range(len(A1)+1)]

for i in range(1, len(A1)+1):
    for j in range(1, len(A2)+1):
        if A2[j-1] == A1[i-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])