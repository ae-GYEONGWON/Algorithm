def solution(players, m, k):
    answer = 0
    server = []
    
    # 증설된 서버는 각자 자기의 수명이 있음.
    # 이용자 수가 초과하면 -> 서버 증설
    # 시간이 지날 때마다 서버 갯수를 업데이트
    # 문제는 서버 갯수를 어떻게 관리할 것인지 -> 각 서버는 각자의 수명이 있기 때문에 별도의 관리가 필요해 보임. => 그럼 각 서버의 수명으로 구분되면 되니까 수명을 저장하자. 그리고 수명이 0이 되면 제거. 이런식으로 업데이트 하면 될듯!
    # 최종 구현 방향
    # 1. 게임 이용자수와 서버 갯수 비교 => 모자라면 증설
    # 2. 다음 시간에 서버 업데이트 이후 비교를 반복
    
    for i, player in enumerate(players):
        
        added_server = player//m - (len(server))
        if added_server > 0:
            server.extend([k for _ in range(added_server)])
            answer += added_server
            
        server = [s-1 for s in server if s > 1]
    return answer