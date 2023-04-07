n = int(input())

ans = 1
if n == 0:
    print(ans)
else:
    for i in range(2,n+1):
        ans *= i
    print(ans)