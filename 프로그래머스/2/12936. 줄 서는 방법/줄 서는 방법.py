from functools import reduce
from math import factorial

def solution(n, k):
    answer = []
    n_list = [i for i in range(1, n+1)]
    
    ans_i = 0
    cnt = 0
    while len(answer) < n:
        n_list_i = 0
        while cnt < k:
            cnt += factorial(n-ans_i-1)
            n_list_i += 1
        
        cnt -= factorial(n-ans_i-1)
        n_list_i -= 1
        answer.append(n_list[n_list_i])
        del n_list[n_list_i]
        ans_i += 1
            
    if n_list:
        answer.append(n_list.pop())
    return answer

def n_factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1), 1)