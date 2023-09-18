import math

def solution(fees, records):
    answer = []
    park_dic = {} # 입출차 관리하는 dic
    ans_dic = {}
    
    records = [record.split(" ") for record in records]
    records.sort(key = lambda x : x[0])
    for record in records:
        time, num, io = record
        h,m = map(int, time.split(":"))
        
        if num in park_dic:
            temp = h*60 + m - park_dic[num]
            if num in ans_dic:
                ans_dic[num] += temp
            else:
                ans_dic[num] = temp
            del park_dic[num]
        else:
            park_dic[num] = h*60 + m

    for i in park_dic.keys():
        if i in ans_dic:
            ans_dic[i] += 1439 - park_dic[i]
        else:
            ans_dic[i] = 1439 - park_dic[i]
    
    print(ans_dic)
    for i in sorted(ans_dic.keys()):
        answer.append(fees[1] + math.ceil(max((ans_dic[i] - fees[0]), 0)/fees[2])*fees[3])
        
        
    return answer