n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
white = 0; blue = 0
def f(map):
    global white, blue
    sum_num = 0; map_size = len(map)
    # 종료 조건
    for i in range(map_size):
        sum_num += sum(map[i])
    if sum_num == 0:
        white += 1
        return
    if sum_num == map_size**2:
        blue += 1
        return
    
    map_size = map_size//2

    side_1 = []; side_2 = []
    for i in map[:map_size]:
        side_1.append(i[:map_size])
        side_2.append(i[map_size:])
    side_3 = []; side_4 = []
    for i in map[map_size:]:
        side_3.append(i[:map_size])
        side_4.append(i[map_size:])
    # 1사분면
    f(side_1)
    # 2사분면
    f(side_2)
    # 3사분면
    f(side_3)
    # 4사분면
    f(side_4)

f(map)
print(white)
print(blue)
