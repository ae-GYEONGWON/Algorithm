def solution(hp):
    answer = 0
    
    if hp%5 == 0:
        return hp//5 + answer
    else:
        answer += hp//5
        hp %= 5
        
    if hp%3 == 0:
        return hp//3 + answer
    else:
        answer += hp//3
        hp %= 3
    
    answer += hp
    
    return answer