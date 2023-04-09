import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    i = int(input())
    dic[i] += 1

for i, j in sorted(dic.items()):
    for _ in range(j):
        print(i)