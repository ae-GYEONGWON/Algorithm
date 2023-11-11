def solution(n, t, m, p):
    answer = ''
    
    total_num = '0'
    for i in range(t*m):
        total_num += to_base_n(n, i)
        
    # print(total_num)
    for i in range(len(total_num)):
        if i%m == p-1:
            answer += total_num[i]
        if len(answer) == t:
            break
    
    return answer

def to_base_n(n, number):
    notation = "0123456789ABCDEF"
    result = ""
    while (number > 0):
        number, mod = divmod(number, n)
        result += str(notation[mod])
    
    return result[::-1]

# 0 1 10 11 100 101 110 111
# 0111
        
        
    