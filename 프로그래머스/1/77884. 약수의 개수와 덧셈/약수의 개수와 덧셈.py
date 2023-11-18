def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        temp = check_num(i)
        if temp % 2 == 0:
            answer += i
        else:
            answer -= i
                
    
    return answer

def check_num(num):
    cnt = 0
    for j in range(1, num+1):
        if num % j == 0:
            cnt += 1
    return cnt  
            