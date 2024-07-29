from heapq import heappush, heappop

def solution(k, score):
    answer = []
    
    heapq = []
    
    for s in score:
        if len(heapq)+1 > k:
            heappush(heapq, s)
            heappop(heapq)
        else:
            heappush(heapq, s)
        
        answer.append(heapq[0])
    
    return answer