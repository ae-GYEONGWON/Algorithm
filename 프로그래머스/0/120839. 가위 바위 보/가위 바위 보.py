def solution(rsp):
    answer = ''
    rsp_dic = {"2": "0", "0": "5", "5": "2"}
    
    return "".join([rsp_dic[i] for i in rsp])