from collections import deque

def solution(skill, skill_trees):
    answer = 0
        
    for skill_tree in skill_trees:
        skill_q = deque(skill)
        is_possible = True
        for s in skill_tree:
            if s in skill_q:
                if s == skill_q[0]:
                    skill_q.popleft()
                else:
                    is_possible = False
                    break
        if is_possible:
            answer += 1
    
    return answer