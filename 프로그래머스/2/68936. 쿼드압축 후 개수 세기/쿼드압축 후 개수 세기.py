def solution(arr):
    answer = [0, 0]
    
    '''
    처음으로 전체가 1이나 0으로만 이루어 졌는지 확인한다.
    반복문을 돌면서 
    4개분면으로 쪼갠다.
    각 분면이 0 또는 1로만 이루어졌는지 확인한다.
    0 또는 1로만 이루어져 있으면 그 분면은 더이상 쪼개지 않고 카운트. 그렇지 않으면 반복해서쪼갠다.
    '''
    N = len(arr)
    # 모든 원소가 1인지 확인
    is_all_ones = all(all(x == 1 for x in row) for row in arr)

    # 모든 원소가 0인지 확인
    is_all_zeros = all(all(x == 0 for x in row) for row in arr)
    
    if N == 2 or is_all_ones or is_all_zeros:
        if is_all_ones or is_all_zeros:
            if arr[0][0] == 0:
                answer = [1, 0]
            else:
                answer = [0, 1]

        elif N == 2 :
            count_0 = sum(row.count(0) for row in arr)
            count_1 = sum(row.count(1) for row in arr)
            answer = [count_0, count_1]

        return answer
    
    while not is_all_zeros and not is_all_ones:
        count_0 = sum(row.count(0) for row in arr)
        count_1 = sum(row.count(1) for row in arr)
        
        rect_1 = [arr[i][:N//2] for i in range(N//2)]
        rect_2 = [arr[i][N//2:] for i in range(N//2)]
        rect_3 = [arr[i][:N//2] for i in range(N//2, N)]
        rect_4 = [arr[i][N//2:] for i in range(N//2, N)]
        
        answer1 = solution(rect_1)
        answer2 = solution(rect_2)
        answer3 = solution(rect_3)
        answer4 = solution(rect_4)
        
        answer[0] = answer1[0] + answer2[0] + answer3[0] + answer4[0]
        answer[1] = answer1[1] + answer2[1] + answer3[1] + answer4[1]
    
        return answer
            