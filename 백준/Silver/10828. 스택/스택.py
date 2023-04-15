import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    order = input().split()
    x = order[0]
    if x == 'push':
        stack.append(int(order[1]))
    elif x == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif x == 'size':
        print(len(stack))
    elif x == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif x == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])