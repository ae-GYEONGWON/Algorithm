import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

no_hear_dic: defaultdict[str, int] = defaultdict(int)
ans_set = set()
for _ in range(n):
    name = input().strip()
    no_hear_dic[name] += 1
    
for _ in range(m):
    name = input().strip()
    
    if no_hear_dic[name] == 1:
        ans_set.add(name)

print(len(ans_set))
for name in sorted(ans_set):
    print(name)