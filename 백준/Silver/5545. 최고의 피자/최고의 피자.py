import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
c = int(input())
d = [int(input()) for _ in range(n)]

d.sort(reverse=True)

now_weight = c
now_cost = a
i = 0
while i < n:
    if now_weight // now_cost <= (now_weight + d[i]) // (now_cost+b):
        now_weight += d[i]; i += 1
        now_cost += b
    else:
        break

print(now_weight//now_cost)