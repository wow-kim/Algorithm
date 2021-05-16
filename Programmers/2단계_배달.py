import heapq
from collections import defaultdict

def solution(N, road, K):
    # 시작점인 1로부터의 거리
    dist = [500001 for i in range(N+1)]
    dist[1] = 0

    # 그래프 생성
    graph = defaultdict(list)
    for i, j, time in road:
        graph[i].append([time, j])
        graph[j].append([time, i])

    # 우선순위 큐
    start = 1
    queue = []
    heapq.heappush(queue, [dist[start], start])

    while queue:
        current_dist, to = heapq.heappop(queue)

        if dist[to] < current_dist:
            continue

        for next_dist, next_to in graph[to]:
            d = current_dist + next_dist
            if d < dist[next_to]:
                dist[next_to] = d
                heapq.heappush(queue, [d, next_to])

    return len([i for i in dist if i <= K])