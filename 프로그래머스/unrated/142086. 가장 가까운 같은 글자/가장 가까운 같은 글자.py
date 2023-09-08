from collections import defaultdict

def solution(s):
    answer = [-1]*len(s)
    dic = dict()
        
    for i, c in enumerate(s):
        # print(dic)
        # print(dic[c])
        if c in dic:
            # print(i, c)
            answer[i] = i-dic[c]
        dic[c] = i
        
    return answer