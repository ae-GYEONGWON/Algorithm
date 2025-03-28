from collections import deque

def solution(dartResult):
    answer_list = []
    alpha_dic = {
        "S": 1,
        "D": 2,
        "T": 3,
    }
    
    # while 문으로 반복에서 score를 빼낸다. 
    # r_type = d(숫자), s(문자), o(옵션)
    # r_type에 따라서 숫자인데 score가 1이면 다음에 0이 나올 수 있고 다른 경우라면 무조건 다음 다른 타입이 나와야 함.(옵션은 없을 수 있음 -> 문자 다음 숫자가 나올 수 있다는 말이네?)
    # 결과에서 파싱한 score을 계산한다. 
    # 계산된 값은 리스트에 저장.
    # 옵션은 리스트 인덱스로 접근해서 계산
    
    DRq = deque(dartResult)
    while DRq:
        r_type = "o"
        score = ""
        while DRq:
            if DRq[0].isdigit():
                if score:
                    break
                if r_type == "o":
                    score += DRq.popleft()
                    r_type = "d"
                # 숫자가 10인 경우
                if r_type == "d" and score == "1":
                    score += DRq.popleft()
            elif DRq[0].isalpha():
                score += DRq.popleft()
            else:
                score += DRq.popleft()
                r_type = "o"
        
        digit = ""
        alpha = ""
        option = ""
        for s in score:
            if s.isdigit():
                digit += s
            elif s.isalpha():
                alpha += s
            else:
                option += s
                
        answer = int(digit) ** alpha_dic[alpha]
        
        if option:
            if option == "*":
                answer *= 2
                if answer_list:
                    answer_list[-1] *= 2
            else:
                answer *= -1

        answer_list.append(answer)
        
        
    return sum(answer_list)