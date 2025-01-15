def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)

    total_box = len(score) // m
    pre_box_num = 0
    for box_num in range(total_box):
        next_box_num = (box_num+1) * m
        answer += min(score[pre_box_num:next_box_num]) * m
        pre_box_num = next_box_num
        
    return answer