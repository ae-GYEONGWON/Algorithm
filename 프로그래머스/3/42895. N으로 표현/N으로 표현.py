def solution(N, number):
    n = str(N)
    # dp 초기화
    dp = [0] + [100]*32000; 
    d = dict(); t=['*','//','+','-']
    # N의 단순 반복 채워놓기
    while int(n)<32000:
        d[len(n)] = d.get(len(n),set()) | {n}
        n+=n[0]
    # i개를 사용해 만들 수 있는 최소의 숫자들 모으기
    for i in range(1,9):
        for j in range(1,i):
            for x in d[j]:
                for y in d[i-j]:
                    for v in t:
                        if 0<(a:=eval(x+v+y))<=32000:
                            dp[a] = min(i,dp[a])
                            # dp를 업데이트 할 때만 사전에 추가
                            if dp[a]==i:
                                d[i] = d.get(i,set())|{str(a)}
        if str(number) in d[i]:
            return i
    return -1