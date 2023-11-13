def solution(n):
    answer = ('수박'*(n//2) if n%2 == 0 else '수박'*((n+1)//2))
    
    return (answer if n%2 == 0 else answer[:-1])