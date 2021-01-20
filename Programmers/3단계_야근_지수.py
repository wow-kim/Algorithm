import heapq
def solution(n, works):
    if n >= sum(works):
        return 0

    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))

    while n > 0:
        a = heapq.heappop(heap)[1]-1
        n -= 1
        heapq.heappush(heap,(-a, a))

    return sum(a[1]**2 for a in heap)