def solution(n):
    answer = 0
    
    if n % 2 == 0:
        for n_ in range(1, n+1):
            if n_ % 2 == 0:
                answer += n_**2
    else:
        for n_ in range(1, n+1):
            if n_ % 2 != 0:
                answer += n_
        
    return answer 