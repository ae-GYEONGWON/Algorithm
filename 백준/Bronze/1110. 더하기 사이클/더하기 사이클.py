N = input()
cnt = 0

if len(N) == 1:
    n = '0'+ N
else:
    n = N
while 1:
    x = str(int(n[0]) + int(n[1]))
    if len(x) == 1:
        x = '0' + x
    n = n[1] + x[1]
    cnt += 1

    if int(n) == int(N):
        break

print(cnt)