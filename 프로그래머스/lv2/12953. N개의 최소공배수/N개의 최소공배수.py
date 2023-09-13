def solution(arr):
    answer = 0
    
    lcm = 0;
    a = arr.pop()
    b = arr.pop()
    # 최소공배수
    def lcm_func(a, b):
        i = 0
        temp = 0
        while True:
            i += 1
            temp = a*i
            if temp % b == 0:
                return temp;
    # print(b, a)
    lcm = lcm_func(b, a)
    # print(lcm)
    while arr:
        temp = arr.pop()
        
        lcm = lcm_func(lcm, temp) if lcm < temp else lcm_func(temp, lcm)
    
    return lcm;