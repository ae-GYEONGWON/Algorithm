import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 두 행렬을 곱하는 함수
def multi_matrix(matrix1, matrix2):
    global n
    new_matrix = [[0]*n for _ in range(n)]
    by_matrix2 = []
    # by_matrix2 = list(zip(*matrix2))
    # 곱해질 행렬 구하기
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(matrix2[j][i])
        by_matrix2.append(temp)

    # 두 행렬 곱하기
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += matrix1[i][k] * by_matrix2[j][k]
            new_matrix[i][j] = temp%1000
    return new_matrix

# 항등원 만들기
unit_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            unit_matrix[i][j] = 1
def f(x):
    if x == 1:
        return multi_matrix(matrix, unit_matrix)
    elif x % 2 == 0:
        temp = f(x//2)
        return multi_matrix(temp, temp)
    else:
        temp = f(x//2)
        return multi_matrix(multi_matrix(temp, temp), matrix)

res = f(b)
for i in res:
    for j in i:
        print(j, end = " ")
    print()