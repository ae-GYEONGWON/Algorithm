def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number+1):
        divisor_cnt = 0
        square_num = int((num)**0.5)
            
        for i in range(1, square_num+1):
            if num % i == 0:
                divisor_cnt += 1
        divisor_cnt *= 2
        if square_num**2 == num:
            divisor_cnt -= 1
        
        # 약수의 갯수를 조건에 맞게 답에 더해준다.
        print(divisor_cnt)
        if divisor_cnt <= limit:
            answer += divisor_cnt
        else:
            answer += power
    return answer