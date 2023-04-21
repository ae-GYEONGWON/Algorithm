import sys
input = sys.stdin.readline
n = int(input()) - 1

def len_s(k):
    if k == 0:
        return 3
    return len_s(k-1)*2 + k + 3

def s(k, n):
    if k == 0:
        if n == 0:
            return 'm'
        else:
            return 'o'
    else:
        l = len_s(k-1)
        if n < l:
            return s(k-1, n)
        elif l <= n < l + k+3:
            if n == l:
                return 'm'
            else:
                return 'o'
        else:
            return s(k-1, n-l-(k+2+1))
k = 0
while True:
    temp = len_s(k)
    if temp > n:
        break
    k += 1

print(s(k, n))