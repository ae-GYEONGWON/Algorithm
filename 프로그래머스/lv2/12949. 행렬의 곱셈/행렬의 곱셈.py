def solution(arr1, arr2):
    answer = [[0]* len(arr2[0]) for _ in range(len(arr1))]
    
    # 0, 0 // 0, 1 & 1, 0 // 1, 1  
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            temp = 0
            for j in range(len(arr2)):
                temp += arr1[i][j] * arr2[j][k]
            answer[i][k] = temp
    
    return answer