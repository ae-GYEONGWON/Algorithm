def solution(s, n):
    answer = ''
    
    for i in s:
        if i == " ":
            answer += " "
        
        if 65 <= ord(i) <= 90:
            new_num = ord(i) + n
            if new_num > 90:
                answer += chr(new_num-26)
            else:
                answer += chr(new_num)
        
        if 97 <= ord(i) <= 122:
            new_num = ord(i) + n
            if new_num > 122:
                answer += chr(new_num-26)
            else:
                answer += chr(new_num)
                
    
    return answer