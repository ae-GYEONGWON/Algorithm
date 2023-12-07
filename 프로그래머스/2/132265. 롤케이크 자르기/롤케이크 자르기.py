from collections import Counter, defaultdict

def solution(topping):
    answer = 0
    
    topping_dic = Counter(topping)
    brother_dic = defaultdict(int)
    
    for t in topping:
        brother_dic[t] += 1
        
        if topping_dic[t] == 1:
            topping_dic.pop(t)
        else:
            topping_dic[t] -= 1
        
        if len(topping_dic) == len(brother_dic):
            answer += 1
    
    
    return answer