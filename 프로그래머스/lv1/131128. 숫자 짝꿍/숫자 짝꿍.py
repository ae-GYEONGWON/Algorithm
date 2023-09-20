from collections import defaultdict

def solution(X, Y):
    answer = ''
    x_dic = defaultdict(int)
    x_list = list(X)
    y_dic = defaultdict(int)
    y_list = list(Y)
    
    for x in x_list:
        x_dic[x] += 1
    for y in y_list:
        y_dic[y] += 1
    
    ans_list = []
    for i in list(set(x_dic.keys()) & set(y_dic.keys())):
        for j in range(min(x_dic[i], y_dic[i])):
            ans_list.append(i)
    
    ans_list.sort(reverse=True)
        
    answer = "".join(ans_list)
    if answer == "":
        return "-1";
    else:
        answer = answer.lstrip("0")
        if answer == "":
            return "0";
        return answer