import sys

input = sys.stdin.readline

n = int(input())

def move(start, end):
    return print('{0} {1}'.format(start, end))

def hanoi(n, a, c):
    # 중간지점
    b = str(6-int(a)-int(c))

    if n == 1:
        move(a, c)
    else:
        hanoi(n-1, a, b)
        move(a, c)
        hanoi(n-1, b, c)
    
print((2**n)-1)
if n <= 20:
    hanoi(n, '1', '3')