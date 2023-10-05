def solution(n):    
    temp = int(n**0.5)
    if temp**2 == n:
        return (temp+1)**2;
    
    return -1;

# def solution(n):    
#     for i in range(1, n+1):
#         if i**2 == n:
#             return (i+1)**2
    
#     return -1;