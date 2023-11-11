# from functools import reduce

# def combination(arr, n):
#     result = []    
#     if n == 0:        
#         return [[]]
#     for i in range(len(arr)):
#         elem = arr[i]        
#         for rest in combination(arr[i + 1:], n - 1):
#             result.append([elem] + rest)    
#     return result

# def solution(clothes):
#     answer = 0
#     arr = []
#     for i in range(len(clothes)):
#         arr.append(clothes[i][1])

#     dic = {}
#     for data in arr:
#         if data in dic:
#             dic[data] += 1
#         else :
#             dic[data] = 1

#     for r in range(1,len(dic.keys())+1):
#         nCr = combination(list(dic.values()), r)
#         for i in range(len(nCr)):
#             if len(nCr[i]) == 1:
#                 answer += nCr[i][0]
#             else:
#                 answer += reduce(lambda x,y: x*y, nCr[i])
    
#     return answer


# from collections import defaultdict
from collections import Counter

# def multiply(arr):
#     ans = 1
#     for n in arr:
#         ans *= n+1
#     return ans

def solution(clothes):
    answer = 1
    arr = []
    
    for i in range(len(clothes)):
        arr.append(clothes[i][1])
    dic = Counter(arr)
    # answer = multiply(dic.values()) - 1
    for value in dic.values():
        answer *= value + 1

    
    return answer - 1


   
            