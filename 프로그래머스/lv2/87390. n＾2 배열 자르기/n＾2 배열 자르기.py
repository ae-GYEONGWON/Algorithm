def solution(n, left, right):
    answer = []
    
    # 행*n+열 = 일차원으로 바꿨을 때의 인덱스
    # 행열에서 각 요소의 값 = 행과 열 중 큰값
    # 7 => 7%n = 1 => 행열은 1부터 시작이므로 3행 2열
    for i in range(left, right+1):
        answer.append(max(i//n+1, i%n+1))
    
    return answer