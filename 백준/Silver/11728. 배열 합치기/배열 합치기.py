import sys
input = sys.stdin.readline

na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in sorted(a+b):
    print(i, end=" ")