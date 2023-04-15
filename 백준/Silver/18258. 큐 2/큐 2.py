import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

def q_push(x):
    queue.append(x)
    return

def q_pop():
    if q_empty():
        return -1
    return queue.popleft()

def q_size():
    return len(queue)

def q_empty():
    if len(queue):
        return 0
    return 1

def q_front():
    if q_empty():
        return -1
    return queue[0]

def q_back():
    if q_empty():
        return -1
    return queue[-1]

n = int(input())
for _ in range(n):
    order = input().split()
    x = order[0]
    if x == 'push':
        q_push(int(order[1]))
    elif x == 'pop':
        print(q_pop())
    elif x == 'size':
        print(q_size())
    elif x == 'empty':
        print(q_empty())
    elif x == 'front':
        print(q_front())
    elif x == 'back':
        print(q_back())
