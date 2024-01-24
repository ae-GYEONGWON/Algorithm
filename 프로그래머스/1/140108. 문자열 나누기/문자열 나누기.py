def solution(s):
    answer = 0
    
    x = s[0]
    x_cnt = 1
    other_cnt = 0
    for i in range(1, len(s)):
        if x_cnt == 0:
            x = s[i]
            x_cnt += 1
            continue
        
        if s[i] != x:
            other_cnt += 1
        else:
            x_cnt += 1
        
        if x_cnt == other_cnt:
            x_cnt = 0
            other_cnt = 0
            answer += 1
    
    if x_cnt and x_cnt != other_cnt:
        answer += 1
    
    return answer