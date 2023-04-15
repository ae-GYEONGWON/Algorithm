import sys
input = sys.stdin.readline
queue = [0]*2000000

front = 0; rear = 0; size = 0

def q_push(x):
    global rear, size, front
    queue[rear] = x
    rear += 1
    size += 1
    return

def q_pop():
    global rear, size, front
    if q_empty():
        return -1
    else:
        value = queue[front]
        front += 1
        size -= 1
        return value
        
def q_size():
    global rear, size, front
    return size

def q_empty():
    global rear, size, front
    if size:
        return 0
    return 1

def q_front():
    global rear, size, front
    if q_empty():
        return -1
    else:
        return queue[front]
    
def q_back():
    global rear, size, front
    if q_empty():
        return -1
    else:
        return queue[rear-1]

n = int(input())
for _ in range(n):
    command = input().split()
    x = command[0]
    if x == 'push':
        q_push(int(command[1]))
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