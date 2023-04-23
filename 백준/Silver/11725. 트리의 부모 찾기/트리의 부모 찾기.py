import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
N = int(input())        
visited = [0] * (N + 1)      
trees = [[] * (N + 1) for _ in range(N + 1)]
parent = [0] * (N + 1) 
for i in range(N-1):                          
    a, b = list(map(int, input().split()))    
    trees[a].append(b)                        
    trees[b].append(a)
    
def dfs(x):
    visited[x] = True
    for i in range(len(trees[x])):
        temp = trees[x][i]
        if not visited[temp]:
            visited[temp] = 1
            parent[temp] = x
            dfs(temp)
    
dfs(1)
for i in parent[2:]:
    print(i)