from collections import defaultdict

def solution(n, works):
    answer = 0
    works_dic = defaultdict(int)
    
    for i in set(works):
        works_dic[i] = works.count(i)
        
    i = max(works_dic.keys())
    while n>0:
        if i == 0:
            break
        if works_dic[i] < n:
            works_dic[i-1] += works_dic[i]
            n -= works_dic[i]
            works_dic[i] = 0
        else:
            works_dic[i-1] += n
            works_dic[i] -= n
            n = 0
        i -= 1


    for key in list(works_dic.keys()):
        answer += (key**2)*works_dic[key]
        
    return answer