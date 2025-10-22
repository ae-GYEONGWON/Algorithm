import sys

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    nums = list(map(int, input().split()))
    graph.append(nums)
    
for i in range(1, n):
    for j in range(i+1):
        graph[i][j] += max(graph[i-1][min(j, i-1)], graph[i-1][max(0, j-1)])

print(max(graph[n-1]))