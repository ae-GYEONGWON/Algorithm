# def solution(nums):
#     answer = 0
#     dic = {}
    
#     for data in nums: # 종류번호와 수를 사전으로 만든다.
#         if data in dic:
#             dic[data] += 1
#         else :
#             dic[data] = 1
        
#     N = len(nums)/2 #max return 값
    
#     if len(dic.keys()) >= N:
#         answer = N
#     else :
#         answer = len(dic.keys())
    
    # return answer























def solution(nums):
    answer = len(nums)//2
    nums_set = set(nums)
    
    return answer if len(nums_set) >= answer else len(nums_set)
