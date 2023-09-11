def solution(s):
    s_list = list(s)
    stack = []
    
    for i in s_list:
        stack.append(i)
        while stack and len(stack) > 1 and len(set(stack[-2:])) == 1:
            stack.pop()
            stack.pop()
    if stack:
        return 0;
    else:
        return 1;