import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [1] + [0]*m

    for coin in coins:
        for i in range(1, m+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[-1])