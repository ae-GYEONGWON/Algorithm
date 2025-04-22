def solution(lottos, win_nums):
    answer = []
    
    num_cnt = 0
    win_nums.sort()
    for num in win_nums:
        if num in lottos:
            num_cnt += 1

    worst = 7 - num_cnt
    best = worst - lottos.count(0)
    
    return [min(best, 6), min(worst, 6)]