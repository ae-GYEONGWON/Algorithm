def solution(n):
    answer = 0
    print(base_to_3_reverse(n))
    return int(base_to_3_reverse(n), 3)

def base_to_3_reverse(num):
    result = ""
    while num > 0:
        num, mod = divmod(num, 3)
        result += str(mod)
    return result