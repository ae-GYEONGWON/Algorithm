from heapq import heapify, heappop, heappush

def solution(N, road, K):
    # 각 마을까지의 최소 비용을 저장할 배열 초기화
    cost = [float('inf')] * (N + 1)
    cost[1] = 0  # 시작점인 1번 마을의 비용은 0

    # 도로 정보 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # 최소힙 초기화 및 시작 노드 추가
    heap = [(0, 1)]  # (비용, 노드)
    heapify(heap)

    while heap:
        current_cost, current_node = heappop(heap)

        # 현재 노드에서 연결된 다른 노드들을 확인
        for next_node, travel_cost in graph[current_node]:
            new_cost = current_cost + travel_cost
            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
                heappush(heap, (new_cost, next_node))
    
    # K 이하로 도달할 수 있는 마을의 수를 계산
    answer = sum(1 for c in cost if c <= K)
    return answer