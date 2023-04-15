from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    if x:
        heappush(heap, (-x, x))
    else:
        if len(heap):
            print(heappop(heap)[1])
        else:
            print(0)