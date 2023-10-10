def solution(num_list):
    answer = 0
    
    sum_even = 0
    sum_odd = 0
    for i, v in enumerate(num_list):
        if i % 2 == 0:
            sum_even += v
        else:
            sum_odd += v
    
    return sum_odd if sum_odd > sum_even else sum_even