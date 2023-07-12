import sys
input = sys.stdin.readline

str_ = list(input().rstrip())
bomb = list(input().rstrip())
bomb_size = len(bomb)
stack = []
str_.reverse()

while (str_):
    stack.append(str_.pop())
    
    while (stack[len(stack)-bomb_size:] == bomb):
        for _ in range(bomb_size):
            stack.pop()
    
if not stack:
    print("FRULA")
else:
    print("".join(stack))