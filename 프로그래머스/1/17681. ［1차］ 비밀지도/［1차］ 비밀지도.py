def solution(n, arr1, arr2):
    answer = []
    
    for num1, num2 in zip(arr1, arr2):
        b_num1 = bin(num1)[2:]
        temp1 = n - len(b_num1)
        if temp1 != 0:
            b_num1 = '0'*temp1 + b_num1
            
        b_num2 = bin(num2)[2:]
        temp2 = n - len(b_num2)
        if temp2 != 0:
            b_num2 = '0'*temp2 + b_num2
        
        res = ''
        for i, j in zip(list(b_num1), list(b_num2)):
            if i == '1' or j =='1':
                res += '#'
            else:
                res += ' '
        
        answer.append(res)
        
        
    return answer