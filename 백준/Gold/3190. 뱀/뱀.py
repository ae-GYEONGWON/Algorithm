import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
t = int(input())
command = [input().split() for _ in range(t)]

q = deque()
q.append([1,1])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time = 0
dir_idx = 0
command_idx = 0

while True:
    time += 1
    x, y = q[-1]
    
    x += dx[dir_idx]; y += dy[dir_idx]
    if [x, y] in q or 1 > x or x > n or 1 > y or y > n:
        break
    if [x, y] in apples:
        q.append([x, y])
        apples.remove([x, y])
    else:
        q.popleft()
        q.append([x, y])
    
    if command_idx < t and time == int(command[command_idx][0]):
        if command[command_idx][1] == "D":
            dir_idx += 1
            dir_idx %= 4
        else:
            dir_idx -= 1
            dir_idx %= 4
        command_idx += 1

print(time)