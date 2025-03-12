def solution(N, stages):
    answer = []

    stage_dic = {
        stage: stages.count(stage)
        for stage in range(1, N+1)
    }
    stages.sort()
    res = []
    for stage in range(1, N+1):
        a = stage_dic[stage]
        b = len([s for s in stages if s>=stage])
        if b == 0:
            rate = 0
        else:
            rate = a/b
        
        res.append((stage, rate))

    res.sort(key = lambda x: (-x[1], x[0]))
    answer = [r[0] for r in res]
    
    return answer