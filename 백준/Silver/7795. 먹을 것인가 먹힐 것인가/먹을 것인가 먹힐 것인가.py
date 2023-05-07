import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    a.sort()
    b.sort(reverse=True)
    for i_a in a:
        for j in range(len(b)):
            if i_a > b[j]:
                ans += len(b)-j
                break
    print(ans)