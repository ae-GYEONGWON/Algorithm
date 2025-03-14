def solution(s, skip, index):
    answer = ''
    
    alpha_list = [chr(code) for code in range(97, 123) if chr(code) not in skip]
    
    # alpha_dict 생성 수정
    alpha_dict = {}
    for idx, alpha in enumerate(alpha_list):
        new_idx = (idx + index) % len(alpha_list)  # 순환 구조 처리
        alpha_dict[alpha] = alpha_list[new_idx]
    
    answer = "".join([alpha_dict[s_] for s_ in s])
    
    return answer
