import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapify(cards)
ans = 0

while len(cards) != 1:
    a = heappop(cards)
    b = heappop(cards)
    ans += a + b
    heappush(cards, a + b)
    

print(ans)