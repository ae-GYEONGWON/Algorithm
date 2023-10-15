def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(idx, sum_num):
        if idx == n:
            if sum_num == target:
                nonlocal answer;
                answer += 1
            return ;

        dfs(idx+1, sum_num+numbers[idx])
        dfs(idx+1, sum_num-numbers[idx])
        return answer;
    
    dfs(0, 0)
    return answer;