n = int(input())
for _ in range(n):
    data = input()
    ans = 0
    score = 0
    for i in data:
        if i == 'O':
            score += 1
            ans += score
        else:
            score = 0
    print(ans)