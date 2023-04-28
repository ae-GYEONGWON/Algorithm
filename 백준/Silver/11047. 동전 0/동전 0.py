import sys

input = sys.stdin.readline
answer = 0
N, K = map(int, input().split())

coin = []
for _ in range(N):
    coin.append(int(input().rstrip()))
# print(N,K,coin)

while K:
    C = coin.pop()
    x = K//C
    if x > 0:
        K -= x*C
        answer += x
print(answer)