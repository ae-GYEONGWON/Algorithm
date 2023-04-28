import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]

bag.sort()
dp = [0]*(k+1)
for i, j in bag:
    for w in range(k, i-1, -1):
        dp[w] = max(dp[w-i]+j, dp[w])
print(max(dp))