import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a=list(map(int,input().split()))

s=0
e=0
ans=a[0]
tmp=0
cnt=0
while (e<n):
    ans+=tmp
    if (ans <= m):
        if ans == m:
            cnt+=1
        e+=1
        if e==n:
            break
        tmp=a[e]
    else:
        tmp=-a[s]
        s+=1

print(cnt)