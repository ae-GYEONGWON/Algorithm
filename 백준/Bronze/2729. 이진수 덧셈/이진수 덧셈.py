import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num1, num2 = input().split()
    print(bin(int(num1, 2) + int(num2, 2))[2:])
    