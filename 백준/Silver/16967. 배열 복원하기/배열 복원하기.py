import sys
input = sys.stdin.readline

h, w, x, y = list(map(int, input().split()))
B = [list(map(int, input().split())) for _ in range(h+x)]

A = [[0]*w for _ in range(h)]

# 위쪽 채우기
for i in range(x):
    for j in range(w):
        A[i][j] = B[i][j]
# 왼쪽채우기
for i in range(x, h):
    for j in range(y):
        A[i][j] = B[i][j]

# 아래쪽 채우기
for i in range(h,h+x):
    for j in range(y, w+y):
        A[i-x][j-y] = B[i][j]

# 오른쪽 채우기
for i in range(x, h+x):
    for j in range(w, w+y):
        A[i-x][j-y] = B[i][j]

# 겹치는 부분 채우기
for i in range(x, h-x):
    for j in range(y, w-y):
        if i == x:
            A[i][j] = B[i][j] - B[i-x][j-y]
        else:
            A[i][j] = B[i][j] - A[i-x][j-y]

for i in A:
    for j in i:
        print(j, end=" ")
    print()