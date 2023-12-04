def solution(n, s):
    answer = []
    
    while s > 0 and n > 0:
        if s//n == 0:
            answer = [-1]
            break
        answer.append(s//n)
        s -= s//n
        n -= 1
    
    return answer