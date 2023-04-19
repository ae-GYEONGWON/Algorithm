import sys
input = sys.stdin.readline

M, N, L = list(map(int, input().split()))
shot_point = list(map(int, input().split()))
animal_position = [list(map(int, input().split())) for _ in range(N)]
ans = 0

shot_point.sort()
for a, b in animal_position:
    start, end = 0, len(shot_point) - 1 
    mid = 0
    while start < end:
        mid = (start + end) // 2
        if shot_point[mid] < a:
            start = mid + 1
        elif shot_point[mid] > a:
            end = mid - 1
        else:
            start = mid
            break
    if abs(shot_point[start]-a) + b <= L:
        ans += 1
    elif start + 1 < len(shot_point) and abs(shot_point[start+1]-a)+b <= L:
        ans += 1
    elif start > 0 and abs(shot_point[start-1]-a)+b <= L:
        ans += 1
print(ans)