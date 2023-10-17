def solution(n, k):
    answer = 0
    
    rev_base = ""
    if k == 10:
        rev_base = str(n)
    else:
        while n > 0:
            n, mod = divmod(n, k)
            rev_base += str(mod)

        rev_base = rev_base[::-1]

    temp = rev_base.split('0')
    print(temp)
    for i in temp:
        if i == "1" or i == "": continue
        temp_num = int(i)
        for j in range(2, int(temp_num**0.5)+1):
            if temp_num % j == 0:
                break
        else:
            answer += 1
            
    return answer