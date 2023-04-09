cnt = 0
n = int(input())
col = [0]*(n+1)

def promising(i):
    k = 1
    while k < i:
        if col[i] == col[k] or abs(col[i]-col[k]) == i-k:
            return False
        k += 1
    return True
    
def n_queens(i):
    global cnt
    if i == n:
        cnt += 1
    else:
        for j in range(1, n+1):
            col[i + 1] = j
            if promising(i+1):
                n_queens(i+1)



n_queens(0)
print(cnt)