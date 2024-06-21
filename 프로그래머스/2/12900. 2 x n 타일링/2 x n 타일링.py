# def solution(n):    
#     '''
#     a1 = 1
#     a2 = 2
#     a3 = 3
#     a4 = 5
#     a5 = 8
#     a6 = 13
#     a8 = 
#     '''
    
#     dp = [1, 1, 2, 3, 5]
    
#     if n < 5:
#         return dp[n]
    
#     for i in range(5, n+1):
#         dp[i] = (dp[i-1] + dp[i-2])%1000000007
    
#     return dp[n]

def solution(n):
    dp = [0 for i in range(n)]
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    return dp[n-1]