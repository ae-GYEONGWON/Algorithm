import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
stack = []
res = [0]*n

for i, top in enumerate(tops):
    while stack and stack[-1][1] <= top:
        stack.pop()
    if stack and stack[-1][1] > top:
        res[i] = stack[-1][0]
    stack.append((i+1, top))

for i in res:
    print(i, end = " ")