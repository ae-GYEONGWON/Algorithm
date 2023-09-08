def solution(land):
    for row_i in range(1, len(land)):
        for col_i in range(len(land[row_i])):
            temp = 0
            for i in range(len(land[row_i-1])):
                if i != col_i:
                    temp = max(temp, land[row_i-1][i])
            land[row_i][col_i] += temp
            
    return max(land[-1])