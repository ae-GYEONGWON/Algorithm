n = int(input())

if n < 100:
    print(n)
elif n == 1000:
    print(144)
else:
    ans = 99
    for i in range(100, n+1):
        new_n = str(i)
        if eval(new_n[0]+'-'+new_n[1]) == eval(new_n[1]+'-'+new_n[2]):
            ans += 1
    print(ans)