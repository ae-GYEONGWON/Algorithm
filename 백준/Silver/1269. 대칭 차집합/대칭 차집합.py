import sys, re
input = sys.stdin.readline

na, nb = map(int, input().split())
a = set(input().split())
b = set(input().split())

print(len(a-b)+len(b-a))