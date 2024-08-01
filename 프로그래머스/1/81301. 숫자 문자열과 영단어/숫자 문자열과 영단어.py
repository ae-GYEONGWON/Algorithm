def solution(s):
    answer = ''
    
    num_dic = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
    
    temp = ''
    for _s in s:
        if _s.isdigit():
            answer += str(_s)
        else:
            if temp in num_dic:
                temp = _s
            else:
                temp += _s
            
            if temp in num_dic:
                answer += str(num_dic[temp])
            
    return int(answer)