import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

l = 0; r = n-1
min = 2000000001
answer = [0,0]
while l < r:
    sum = data[l]+data[r]
    if abs(sum) < min:
        answer[0] = data[l]
        answer[1] = data[r]
        min = abs(sum)
    if sum == 0:
        break

    if sum < 0:
        l += 1
    else:
        r -= 1

print(answer[0], answer[1])