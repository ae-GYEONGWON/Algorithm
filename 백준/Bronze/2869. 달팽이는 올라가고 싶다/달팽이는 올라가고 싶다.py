a, b, v = map(int, input().split())

now = 0
ans = 1
now += a
move = a - b

new_v = v-a

now += (new_v//move)*move
ans += (new_v)//move

if now == v:
    print(ans)
else:
    print(ans+1)