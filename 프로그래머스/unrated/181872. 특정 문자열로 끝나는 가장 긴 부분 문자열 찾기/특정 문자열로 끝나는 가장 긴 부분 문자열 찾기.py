def solution(myString, pat):
    answer = ''
    
    idx = len(myString)-1
    while True:
        while myString[idx] != pat[-1]:
            idx -= 1;
        if myString[idx-len(pat)+1:idx+1] == pat:
            return "".join(myString[:idx+1])