# import itertools

# def solution(numbers):
#     answer = 0
#     arr =[]
#     n = list(numbers)
#     N = list(map(int,n))
#     p = []
#     print(N)
#     for r in range(len(N)+1):
#         nPr = itertools.permutations(N, r)
#     for i in range(len(list(set(list(nPr))))):
#         p.append(list(list(set(list(nPr)))[i]))
#     print(list(nPr))
#     for i in range(len(p)):
#         a = ''
#         for j in p[i]:
#             a += j
#         arr.append(a)
#     print(arr)
    
#     return answer









# import itertools

# def solution(numbers):
#     answer = 0
#     N = len(numbers)
#     nPr = []
#     for r in range(1,N+1):
#         nPr.extend(list(itertools.permutations(numbers, r)))
#     # print(nPr)
#     for i in range(len(nPr)):
#         nPr[i] = int("".join(nPr[i]))
#     nPr = list(set(nPr))
    
#     for num in nPr:
#         if num in [0, 1]: continue
#         if num in [2, 3]: answer += 1
#         for i in range(2,int((num**0.5))+1):
#             if num%i == 0: break
#             if i == int(num**0.5) and num%i != 0:
#                 answer += 1
#     return answer

# print(solution("1231"))







from itertools import permutations

def solution(numbers):
    nPr_list = [permutations(numbers, i+1) for i in range(len(numbers))]
    num_candi_set = set()
    for nPr in nPr_list:
        nPr_mapped = list(map(list, nPr))
        for e in nPr_mapped:
            num_candi_set.add(int("".join(e)))

    return len([num for num in num_candi_set if check_prime(num)])

def check_prime(num):
    if num in [0, 1]:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    else:
        return True
            







