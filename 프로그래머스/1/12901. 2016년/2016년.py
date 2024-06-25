def solution(a, b):    
    '''
    a = 1~12
    b = 1~29(윤년) or 1~30 or 1~31
    '''
    
    months_dic = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    answer_dic = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE", 5: "WED", 6: "THU"}
    
    days = -1 + b
    for month in range(1, a):
        days += months_dic[month]
        
    days %= 7
    
    return answer_dic[days]