import sys
input =sys.stdin.readline

n = int(input())
num = input().rstrip()
res = 0

for i in range(n):
    res += int(num[i])

print(res)