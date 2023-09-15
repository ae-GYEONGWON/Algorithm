from collections import deque

def solution(s):
    answer = 0
    
    q = deque(s)
    x = 0
    
    while x < len(s):
        stack = []
        for i in q:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            elif i == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif i == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif i == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                break
        else:
            if not stack:
                answer += 1        
        
        temp = q.popleft()
        q.append(temp)
        x += 1
        
    
    return answer