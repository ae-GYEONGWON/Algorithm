import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))
coins = [int(input()) for _ in range(n)]

dp = [0] * (k+1)

for coin in coins:
    for i in range(1, len(dp)):
        if i-coin > 0:
            if dp[i] == 0 or dp[i] == -1:
                if dp[i-coin] == -1:
                    dp[i] = -1
                else:
                    dp[i] = dp[i-coin] + 1
            else:
                if dp[i-coin] == -1:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        # i와 coin이 같으므로 동전 한개로 i원을 만들 수 있음.
        elif i-coin == 0:
            dp[i] = 1
        elif i-coin < 0 and dp[i] == 0:
            dp[i] = -1
print(dp[k])