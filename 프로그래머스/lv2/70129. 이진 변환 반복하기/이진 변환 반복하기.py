def solution(s):    
    total_removed_0 = 0
    depth = 0
    
    while s != "1":
        count_1 = s.count("1")
        total_removed_0 += len(s) - count_1
        s = format(count_1, "b")
        depth += 1

    return [depth, total_removed_0]