import sys

input = sys.stdin.readline

n, m = map(int, input().split())

money_list = [int(input()) for _ in range(n)]

start = max(money_list)
end = sum(money_list)
answer = 0
while start <= end:
    mid = (start + end)//2
    
    total=0
    cnt=0
    for x in money_list:
        if total+x<=mid:
            total+=x
        else:
            cnt+=1
            total=0
            total+=x
    if total:
        cnt+=1

    if cnt>m:
        start=mid+1
    else:
        end=mid-1
        answer=mid
        
print(answer)