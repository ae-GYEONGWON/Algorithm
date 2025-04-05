def solution(n_str):
    if n_str[0] != "0":
        return n_str
    
    target = ""
    for s in n_str:
        if s != "0":
            target = s
            break
    target_idx = n_str.index(target)
    return n_str[target_idx:]