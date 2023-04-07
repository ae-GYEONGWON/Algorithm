w, h = map(int, input().split())
n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
line = sorted(line, key = lambda x: (x[0], x[1]))
# for문을 돌면서 직전 값을 저장해줄 변수
dx = 0; dy = 0
# 잘려진 종이의 가로와 세로의 최대길이
max_w = 0; max_h = 0
for i in line:
    a, b = i
    if a == 0:
        if max_h < b-dy:
            max_h = b-dy
        dy = b
    else:
        if max_w < b-dx:
            max_w = b-dx
        dx = b
print(max(w-dx, max_w)*max(h-dy, max_h))