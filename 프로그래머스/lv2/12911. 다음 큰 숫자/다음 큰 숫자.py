def solution(n):
    answer = 0
    
    n_b = format(n, "b").count("1")
    next = n
    while True:
        next += 1
        if n_b == format(next, "b").count("1"):
            answer = next
            break
    
    return answer