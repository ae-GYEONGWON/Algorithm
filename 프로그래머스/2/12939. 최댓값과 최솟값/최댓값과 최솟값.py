def solution(s):
    answer = ''
    
    num_list = sorted(list(map(int, s.split(" "))))
    # print(num_list)
    answer += str(num_list[0]) + " " + str(num_list[-1])
    
    return answer