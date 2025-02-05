from itertools import combinations as cb

def solution(nums):
    cb_list = list(cb(nums, 3))
    
    def check_prime_number(num):
        res = False
        for x in range(2, int(num**0.5)+1):
            if num % x == 0:
                break
        else:
            res = True
        return res
    
    cnt = 0
    for cb_e in cb_list:
        if check_prime_number(sum(cb_e)):
            cnt += 1
    
    answer = cnt
    return answer