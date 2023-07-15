import sys
input = sys.stdin.readline

T = int(input())
if T % 10:
    print(-1)
else:
    ans = [0, 0, 0]
    
    if T >= 300:
        ans[0] = T // 300
        T = T%300
    if T >= 60:
        ans[1] = T//60
        T = T%60
    if T >= 10:
        ans[2] = T//10

    for i in ans:
        print(i, end=" ")