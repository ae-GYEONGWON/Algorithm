import sys

input = sys.stdin.readline

line = input().rstrip()

stack = []

for s in line:
    stack.append(s)
    if len(stack) >= 4:
        if stack[len(stack)-4:] == ['P','P','A','P']:
            for _ in range(3):
                stack.pop()

if ''.join(stack) == 'P':
    print('PPAP')
else :
    print('NP')