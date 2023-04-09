from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

nPr = list(permutations(arr, n))

max_sum = 0
for i in nPr:
    
    sum_i = 0
    for j in range(1,len(i)):
        sum_i += abs(i[j-1]-i[j])

    if sum_i > max_sum:
        max_sum = sum_i

print(max_sum)