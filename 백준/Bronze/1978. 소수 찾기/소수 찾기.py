n = int(input())
data = list(map(int, input().split()))
ans = 0

for i in range(n):
    if data[i] == 1: continue
    x = int((data[i])**0.5)
    j = 2
    if x == 1:
        ans += 1
    else:
        while 1:
            if data[i]%j == 0:
                break
            if j == x:
                ans += 1
                break
                
            if j < x:
                j += 1

print(ans)