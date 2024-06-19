def solution(m, n, board):
    answer = 0
    
    board = list(map(list, zip(*board)))
    
    while True:
        check_set = set()
        for row in range(m-1):
            for col in range(n-1):
                if board[col][row] != "" and board[col][row] == board[col+1][row] == board[col][row+1] == board[col+1][row+1]:
                    check_set.add((col, row))
                    check_set.add((col+1, row))
                    check_set.add((col, row+1))
                    check_set.add((col+1, row+1))


        answer += len(check_set)

        for col, row in check_set:
            board[col][row] = ""

        for col in range(n):
            empty = ["" for block in board[col] if block==""]
            board[col] = empty + [block for block in board[col] if block!=""]


        if len(check_set) == 0:
            break
        
    
    return answer
    