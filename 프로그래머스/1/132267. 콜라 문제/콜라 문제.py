def solution(a, b, n):
    answer = 0
    
    while n >= a:
        taken_coke = (n//a) * b
        answer += taken_coke
        n = taken_coke + n%a
    
    return answer