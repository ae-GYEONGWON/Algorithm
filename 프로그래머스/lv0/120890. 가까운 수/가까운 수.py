def solution(array, n):
    answer = 0
    
    temp = 1000
    for i in array:
        if temp > abs(i-n):
            temp = abs(i-n)
            answer = i
        elif temp == abs(i-n):
            if answer > i:
                answer = i
    
    return answer