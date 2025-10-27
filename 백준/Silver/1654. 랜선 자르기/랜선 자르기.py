import sys
import math

input = sys.stdin.readline

# 입력받기
N, K = map(int, input().split())
wires = [int(input().rstrip()) for _ in range(N)]

wires.sort()
start = 1
end = wires[-1]

while start <= end:
    cnt = 0
    mid = (start + end)// 2
    cnt = sum([math.floor(wire/mid) for wire in wires])
    if cnt >= K:
        start = mid + 1
    else :
        end = mid - 1

# 최대 랜선의 길이 이므로 end를 출력(2 8 / 2 / 8)
print(end)