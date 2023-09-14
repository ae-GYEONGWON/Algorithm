# def solution(want, number, discount):
#     answer = 0
#     dis_dic = dict()
    
#     for i in discount[:min(len(discount), 10)]:
#         if i in dis_dic:
#             dis_dic[i] += 1
#         else:
#             dis_dic[i] = 1
            
#     today = 0
#     while today+10 < len(discount):
#         for i in range(len(want)):
#             if want[i] in dis_dic:
#                 if dis_dic[want[i]] != number[i]: break;
#             else: break
#         else:
#             print(today)
#             answer += 1
        
#         dis_dic[discount[today]] -= 1
#         if discount[today+10] in dis_dic:
#             dis_dic[discount[today+10]] += 1
#         else:
#             dis_dic[discount[today+10]] = 1
#         today += 1
    
#     return answer

def solution(want, number, discount):
    answer = 0
    N = len(discount)
    disc_i = 0

    while disc_i + 10 <= N:
        avail_disc = discount[disc_i:disc_i+10]

        if all(num == avail_disc.count(product) for product, num in zip(want, number)):
            answer += 1

        disc_i += 1


    return answer