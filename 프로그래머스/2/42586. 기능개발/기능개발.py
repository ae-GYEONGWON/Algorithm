# def solution(progresses, speeds):
#     answer = []
#     count = 0
#     while progresses:
#         progresses = [progresses[i] + speeds[i] for i in range(len(speeds))]
#         while progresses[0] >= 100:
#             count += 1
#             progresses.pop(0)
#             speeds.pop(0)
#             if len(progresses) == 0:
#                 break
#         if count != 0:
#             answer.append(count)
#             count = 0
            
            
#     return answer













from collections import deque

def solution(progresses, speeds):
    answer = []
    
    p_q = deque(progresses)
    s_q = deque(speeds)
    while p_q:
        cnt = 0
        for i, p in enumerate(p_q):
            p_q[i] += s_q[i]
        
        while p_q:
            if p_q[0] >= 100:
                p_q.popleft()
                s_q.popleft()
                cnt += 1
            else:
                break
                
        if cnt:
            answer.append(cnt)
    
    return answer



