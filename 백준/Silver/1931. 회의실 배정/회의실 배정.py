import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key = lambda x : (x[1], x[0]))

ans = 1
now_e = data[0][1]
for i in range(1, n):
    if now_e <= data[i][0]:
        now_e = data[i][1]
        ans += 1
print(ans)