# def solution(n):    
    # # a[n] = a[n//2] or a[n-1]+1
    # # a[1]부터 a[n]까지 최소값을 업데이트 해보자
    # # a[1] = 1, a[2] = 1, a[3] = 2, a[4] = 1, a[5] = 2, a[6] = 2, a[7] = 3,
    # # a[5000] = a[2500] = a[1250] = a[625] = a[312]+1 = a[156]+1 = a[78]+1
    # # = a[39] + 1 = a[19] + 2 = a[9] + 3 = a[4] + 4
    # dp = [0, 1, 1] + [0]*(n-2)
    # for i in range(3, n+1):
    #     if i % 2 == 0:
    #         dp[i] = dp[i//2]
    #     else:
    #         dp[i] = dp[(i-1)//2]+1
    # return dp[n]

#     answer = 0
    
#     while True:
#         if n == 1:
#             return answer+1
        
#         if n % 2 != 0:
#             answer +=1
#         n //= 2        


def solution(n):
    return bin(n)[2:].count('1')