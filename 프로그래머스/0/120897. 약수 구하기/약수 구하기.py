def solution(n):
    answer = []
    
    for e in range(1, int(n**0.5)+1):
        if n % e == 0:
            answer.extend([e, n//e]) if e != n//e else answer.append(e)

    answer.sort()
    return answer