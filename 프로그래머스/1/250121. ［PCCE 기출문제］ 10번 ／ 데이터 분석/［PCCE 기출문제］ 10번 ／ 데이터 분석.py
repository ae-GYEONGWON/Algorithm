# 문제 이해하는 데 5분

def solution(data, ext, val_ext, sort_by):
    answer = []
    
    data_dic = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    ext_idx = data_dic[ext]
    for i in range(len(data)):
        if data[i][ext_idx] < val_ext:
            answer.append(data[i])
    
    sort_by_idx = data_dic[sort_by]
    return sorted(answer, key= lambda x : x[sort_by_idx])