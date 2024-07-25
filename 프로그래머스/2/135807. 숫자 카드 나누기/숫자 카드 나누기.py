# def solution(arrayA, arrayB):
#     answer = 0
    
#     arrayA = set(arrayA)
#     arrayB = set(arrayB)
    
#     gcd1 = gcd(arrayA)
#     gcd2 = gcd(arrayB)
    
#     for eleB in arrayB:
#         if eleB%gcd1==0:
#             break
#     else:
#         answer = max(answer, gcd1)
        
#     for eleA in arrayA:
#         if eleA%gcd2==0:
#             break
#     else:
#         answer = max(answer, gcd2)
    
#     return answer

# def gcd(args_list):
#     for num in range(max(args_list), 1, -1):
#         for arg in args_list:
#             if not (arg % num == 0):
#                 break
#         else:
#             return num
#     else:
#         return 1

from math import gcd
from functools import reduce


def solution(a, b):
    a, b = list(set(a)), list(set(b))

    findGCD = lambda array: reduce(lambda acc, cur: gcd(acc, cur), array, 0)
    checkGCD = lambda array, GCD: GCD if all(e % GCD != 0 for e in array) else 0

    gcdA, gcdB = checkGCD(b, findGCD(a)), checkGCD(a, findGCD(b))

    return 0 if not (gcdA or gcdB) else max(gcdA, gcdB)