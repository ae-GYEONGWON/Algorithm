import sys
input = sys.stdin.readline
k = int(input())

stack = [0]*100000
ptr = 0
for i in range(k):
    num = int(input())
    if num == 0:
        stack[ptr-1] = 0
        ptr -= 1
    else:
        stack[ptr] = num
        ptr += 1
print(sum(stack))