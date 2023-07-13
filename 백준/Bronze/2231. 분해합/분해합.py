import sys 
input = sys.stdin.readline

N = int(input())
ans = 0
for num in range(N-1, 0, -1):
    res = num + sum([int(str(num)[i]) for i in range(len(str(num)))])
    
    if res == N:
        ans = num

print(ans)