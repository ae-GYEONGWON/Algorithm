from itertools import permutations

n, m = map(int, input().split(' '))

num_list = [str(num) for num in range(1, n+1)]

nPr = permutations(num_list, m)

for res in nPr:
    print(' '.join(res))