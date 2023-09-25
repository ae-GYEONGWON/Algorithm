def solution(p):
    if p == "":
        return ""
    # u, v로 분리하는 함수
    u = ""
    v = ""
    open_brakets = 0
    close_brakets = 0
    for i, braket in enumerate(p):
        if braket == "(":
            open_brakets += 1
        elif braket == ")":
            close_brakets += 1
        if open_brakets == close_brakets:
            u = p[:i+1]
            v = p[i+1:]
            break
    # u가 올바른 괄호 문자열인지 확인
    stack = []
    flag = False
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                flag = False
                break
    else:
        if not stack:
            flag = True
    # u가 올바른 괄호 문자열이 아니라면 -> 올바른 괄호로 바꿔줌.
    if flag == False:
        new_str = ""
        for i in u[1:-1]:
            if i == "(":
                new_str += ")"
            else:
                new_str += "("
        return "(" + solution(v) + ")" + new_str
    return u + solution(v)
    
    # v를 재귀
    # 올바른 괄호 문자열인지 확인하는 함수
    # 아래 두가지를 재귀 하는 함수