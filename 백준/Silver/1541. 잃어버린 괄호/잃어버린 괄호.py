import sys
input = sys.stdin.readline

data = list(input().rstrip().split('-'))
ans = 0
for i in data[0].split('+'):
    ans += int(i)
if len(data) == 1:
    print(ans)
else:
    for i in range(1, len(data)):
        for j in data[i].split('+'):
            ans -= int(j)
    print(ans)