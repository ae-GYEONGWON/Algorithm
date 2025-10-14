from heapq import heappush, heappop
import sys

input = sys.stdin.readline
heap = []

n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            min_num = heappop(heap)
            print(min_num)
        continue
    heappush(heap, num)
