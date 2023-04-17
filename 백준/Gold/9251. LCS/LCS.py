a = input()
b = input()

lst = [0]*(len(a)+1)
for x in range(len(a)+1):
    lst[x] = [0]*(len(b)+1)

for x in range(len(a)):
    for y in range(len(b)):
        if a[len(a)-x-1] == b[len(b)-y-1]:
            lst[len(a)-x-1][len(b)-y-1] = lst[len(a)-x][len(b)-y]+1
        else:
            lst[len(a)-x-1][len(b)-y-1] = max(lst[len(a)-x-1][len(b)-y],lst[len(a)-x][len(b)-y-1])
print(lst[0][0])