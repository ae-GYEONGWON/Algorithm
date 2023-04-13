from itertools import combinations_with_replacement as combi

t = int(input())
cases = [int(input()) for _ in range(t)]
nums = [1,2,3]

def sol(x):
    global sum, case, ans
    if x == 0:
        ans += 1
        return 
    
    for i in nums:
        if sum + i <= case:
            sum += i
            sol(x-i)
            sum -= i

for case in cases:
    ans = 0
    sum = 0
    sol(case)
    print(ans)

# 5 : 1 1 1 1 1, 2 1 1 1, 1 2 1 1 , 1 1 2 1, 1 1 1 2, 2 2 1, 2 1 2, 1 2 2, 1 1 3, 1 3 1, 3 1 1, 2 3, 3 2