height = [int(input()) for _ in range(9)]

for i in range(9):
    if i == 8:
        temp = height[:8]
    else:
        temp = height[0:i]+height[min(i+1, 8):]
    for j in range(8):
        if j == 7:
            ans = temp[:7]
        else:
            ans = temp[0:j]+temp[min(j+1, 7):]
        
        if sum(ans) == 100:
            ans.sort()
            for k in ans:
                print(k)
            exit(0)