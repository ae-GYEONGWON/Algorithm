import sys
from collections import deque
import math
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
A = list(map(int, input().split()))
A = A[::-1]
operator_list = list(map(int, input().split()))
opstack = deque()

def cal(opstack):
    global A
    B = copy.deepcopy(A)
    for x in opstack:
        if x == 0:
            B.append(B.pop()+B.pop())
        elif x == 1:
            B.append(B.pop()-B.pop())
        elif x == 2:
            B.append(B.pop()*B.pop())
        else:
            a = B.pop()
            b = B.pop()
            if a < 0:
                c = -a//b
                B.append(-c)
            else:
                B.append(a//b)
    return B[0]

max_res = -math.inf; min_res = math.inf
def dfs(operator):
    global max_res, min_res
    # 하나의 식이 완성되면 종료
    if sum(temp_oper_list) == 0:
        res = cal(opstack)
        if res > max_res:
            max_res = res
        if res < min_res:
            min_res = res
        return
    
    for i in range(4):
        if temp_oper_list[i]:
            opstack.append(i)
            temp_oper_list[i] -= 1
            dfs(temp_oper_list[i])
            opstack.pop()
            temp_oper_list[i] += 1

for i in range(4):
    temp_oper_list = copy.deepcopy(operator_list)
    if temp_oper_list[i]:
        temp_oper_list[i] -= 1
        opstack.append(i)
        dfs(i)
        temp_oper_list[i] += 1
        opstack.pop()

print(max_res)
print(min_res)