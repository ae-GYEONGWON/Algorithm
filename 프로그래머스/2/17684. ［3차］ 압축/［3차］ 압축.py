from collections import defaultdict

def solution(msg):
    answer = []
    
    # A / B / 1 / 27 : AB
    # B / A / 2 / 28 : BA
    # AB / A / 27 / 29 : ABA
    # ABA / B / 29 / 30 : ABAB
    # BA / B / 28 / 31 : BAB
    # BAB / A / 31 / 31 : BABA
    # ABAB /  / 30 / -
    alpha_dic = defaultdict()
    start_alpha = 'A'
    for i in range(26):
        alpha_dic[chr(ord(start_alpha)+i)] = ord(start_alpha)-64+i
    
    s = 0; e = 1; num = 27
    while e <= len(msg):
        while e < len(msg) and msg[s:e] in alpha_dic:
             e += 1

        if msg[s:e] not in alpha_dic:
            e -= 1
        answer.append(alpha_dic[msg[s:e]])
        if e < len(msg):
            alpha_dic[msg[s:e+1]] = num
            num += 1
        else:
            break
        s = e
        e += 1
        
        
    
    return answer