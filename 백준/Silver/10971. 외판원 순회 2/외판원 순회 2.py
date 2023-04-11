import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

matrix = [list(map(int,input().split())) for _ in range(n)]
answer = 10000000
for i in permutations(range(1,n),n-1):
    num_list = [*i]
    
    # 처음과 끝에 1번 도시를 넣는다
    num_list = [0] + num_list + [0]

    sub = 0
    
    # for else 구문을 사용하여 경로가 없을 때를 제외한다
    for j in range(n) :
        cost = matrix[num_list[j]-1][num_list[j+1]-1]
        if cost == 0 :
            break
        else :
            sub += cost
    	
        # 이미 sub가 answer 이상이면 반복문을 멈춘다
        if sub > answer :
            break
            
    else:
        if answer > sub:
            answer = sub
print(answer)