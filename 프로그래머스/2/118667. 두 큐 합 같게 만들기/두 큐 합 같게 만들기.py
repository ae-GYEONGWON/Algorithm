from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    target_num = (sum_q1 + sum_q2)//2

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    limit = 3*(len(queue1)) -3
    while sum_q1 != sum_q2:
        
        if sum_q1 > sum_q2:
            num = queue1.popleft()
            sum_q1 -= num
            sum_q2 += num
            queue2.append(num)
        elif sum_q1 < sum_q2:
            num = queue2.popleft()
            sum_q1 += num
            sum_q2 -= num
            queue1.append(num)
        
        answer += 1
        
        if answer > limit:
            return -1
    
    return answer