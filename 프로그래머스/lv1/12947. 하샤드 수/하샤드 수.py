def solution(x):
    answer = True
    
    temp = list(str(x))
    sum_n = 0
    
    for i in temp:
        sum_n += int(i)
    if x % sum_n == 0:
        return True
    
    return False