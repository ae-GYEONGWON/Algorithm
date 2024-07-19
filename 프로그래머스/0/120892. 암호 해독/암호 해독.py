def solution(cipher, code):
    answer = ''
    
    idx = code-1
    while idx < len(cipher):
        answer += cipher[idx]
        idx += code
    
    return answer