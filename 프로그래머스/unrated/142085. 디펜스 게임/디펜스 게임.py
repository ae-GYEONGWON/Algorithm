from heapq import heapify, heappushpop

def solution(n, k, enemy):
    mujeok = enemy[:k]
    heapify(mujeok)

    for i, ene in enumerate(enemy[k:]):
        n -= heappushpop(mujeok, ene)
        if n < 0:
            return i+k;
    return len(enemy)