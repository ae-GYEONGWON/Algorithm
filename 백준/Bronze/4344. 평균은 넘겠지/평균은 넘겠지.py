c = int(input())
for _ in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    if n == 1:
        print('0.000%')
    else:
        avg = sum(data[1:])/n
        # 평균을 넘는 학생수 a
        a = 0
        for i in data[1:]:
            if i > avg:
                a += 1
        print(f'{round(a/n*100, 3):.3f}%')