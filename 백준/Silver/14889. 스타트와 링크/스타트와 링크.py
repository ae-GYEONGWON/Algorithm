import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())

graph = []
ans = float("inf")
for _ in range(n):
    graph.append(list(map(int, input().split())))

num_set = set(n for n in range(n))
first_cor = combinations(num_set, n//2)

for fc in first_cor:
    fc_combi = combinations(fc, 2)
    first_score = 0
    for i1, i2 in fc_combi:
        first_score += (graph[i1][i2] + graph[i2][i1])
    sec_num_set = num_set - set(fc)
    sec_combi = combinations(sec_num_set, 2)
    sec_score = 0
    for i1, i2 in sec_combi:
        sec_score += (graph[i1][i2] + graph[i2][i1])
    ans = min(ans, abs(sec_score - first_score))
        
print(ans)