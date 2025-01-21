from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = defaultdict(list)
        
    orders.sort(key=lambda x : -len(x))
    max_len_order = len(orders[0])
    
    for c_cnt in course:
        order_cnt = 0
        max_order_cnt = 0
        if max_len_order < c_cnt:
            break
            
        for idx, order in enumerate(orders):
            if len(order) < c_cnt:
                break
            
            nCr = combinations(order, c_cnt)
            combi_list = ["".join(c) for c in nCr]
            
            temp_orders_list = orders[:idx] + orders[idx+1:]
            # print(orders)
            # print(temp_orders_list)
            # print()
            for combi in combi_list:
                for temp_order in temp_orders_list:
                    if all([c in temp_order for c in combi]):
                        order_cnt += 1
                if order_cnt > 0:
                    if max_order_cnt == order_cnt:
                        answer[c_cnt].append(combi)
                    elif max_order_cnt < order_cnt:
                        answer[c_cnt].clear()
                        answer[c_cnt].append(combi)
                        max_order_cnt = order_cnt
                order_cnt = 0
    answer_list = []
    for v in answer.values():
        answer_list.extend(v)

    setted_answer = list(set(answer_list))
    new_answer_list = [] 
    for e in setted_answer:
        temp_list = list(e)
        temp_list.sort()
        new_answer_list.append("".join(temp_list))
        
    return sorted(list(set(new_answer_list)))