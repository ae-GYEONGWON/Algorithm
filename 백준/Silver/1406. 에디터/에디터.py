import sys
from collections import deque
input = sys.stdin.readline

l_str = deque(input().rstrip())
r_str = deque()
n = int(input())

for _ in range(n):
    com_line = input().split()
    x = com_line[0]

    if x == "L" and l_str:
        r_str.appendleft(l_str.pop())
    elif x == "D" and r_str:
        l_str.append(r_str.popleft())
    elif x == "B" and l_str:
        l_str.pop()
    elif x == "P":
        l_str.append(com_line[1])

print("".join(l_str+r_str))