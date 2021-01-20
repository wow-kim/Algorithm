import heapq
def solution(A, B):
    heapq.heapify(A)
    heapq.heapify(B)
    point = 0
    while A:
        a = heapq.heappop(A)
        while B:
            b = heapq.heappop(B)
            if a < b:
                point += 1
                break
    return point