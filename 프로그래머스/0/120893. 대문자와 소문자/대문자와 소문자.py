def solution(my_string):
    answer = ''
    
    for s in my_string:
        if ord(s) < 97:
            answer += s.lower()
        else:
            answer += s.upper()
    
    return answer