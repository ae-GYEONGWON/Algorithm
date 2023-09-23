# def solution(n):    
#     row = [0]*n
#     def is_promising(x):
#         for i in range(x):
#             if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
#                 return False
#         return True
    
#     def n_queen(x):
#         if x == n:
#             return 1;
        
#         cnt = 0
#         for i in range(n):
#             row[x] = i
#             if is_promising(x):
#                 cnt += n_queen(x+1)
#         return cnt
                
#     return n_queen(0)

def solution(n):
	# 어태까지의 queen 위치 ls, 내가 두려는 위치 new
    def check(ls, new):
        for i in range(len(ls)):
        	# 같은 열에 퀸을 둔 적이 있거나, 대각 위치에 둔 적이 있다면, return False
            if new == ls[i] or (len(ls)-i) == abs(ls[i]-new):
                return False
        return True
    def dfs(n, ls):
    	# 끝 행까지 도달! return 1
        if len(ls) == n:
            return 1
        # 끝 행이 아니라면, 다음 줄을 다시 탐색
        cnt = 0
        for i in range(n):
            if check(ls, i):
                cnt += dfs(n, ls+[i])
        # 탐색 결과를 return
        return cnt
        
    return dfs(n, [])