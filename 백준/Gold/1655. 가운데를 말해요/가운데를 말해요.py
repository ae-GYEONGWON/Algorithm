import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

n = int(input())
min_heap = []
max_heap = []
# 중간값

# for _ in range(n-1):
#     num = int(input())
#     if center < num:
#         heappush(min_heap, num)
#     else:
#         heappush(max_heap, -num)

#     if len(max_heap)+1 < len(min_heap):
#         temp = heappop(min_heap)
#         if center < temp:
#             heappush(max_heap, -center)
#             center = temp
#         else:
#             heappush(min_heap, temp)

#     print(center)


for _ in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)
    
    if min_heap and -max_heap[0] > min_heap[0]:
        a = - heappop(max_heap)
        b = heappop(min_heap)
        heappush(max_heap, -b)
        heappush(min_heap, a)

    print(-max_heap[0])