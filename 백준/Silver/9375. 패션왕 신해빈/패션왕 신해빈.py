import sys
from collections import defaultdict

input = sys.stdin.readline

test_case_cnt = int(input())

for _ in range(test_case_cnt):
    n = int(input())
    clothes_dict = defaultdict(list)
    for _ in range(n):
        cloth, kind = input().split()
        clothes_dict[kind].append(cloth)
        
    ans = 1
    for v in clothes_dict.values():
        ans *= len(v) + 1
    print(ans - 1)