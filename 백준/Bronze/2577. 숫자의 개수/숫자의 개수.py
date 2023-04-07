a = int(input())
b = int(input())
c = int(input())

d = a*b*c
ans = [0]*10
for i in str(d):
    ans[int(i)] += 1

for i in ans:
    print(i)