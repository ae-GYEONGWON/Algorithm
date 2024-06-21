def solution(n):    
    '''
    a1 = 1
    a2 = 2
    a3 = 3
    a4 = 5
    a5 = 8
    a6 = 13
    a8 = 
    '''
    
    a = 1; b = 1
    
    for _ in range(n):
        a, b = b, (a+b)%1000000007
    
    return a

# def solution(n):
#     dp = [0 for i in range(n)]
#     dp[0], dp[1] = 1, 2
#     for i in range(2, n):
#         dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

#     return dp[n-1]