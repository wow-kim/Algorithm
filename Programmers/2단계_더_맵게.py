import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while True:

        f1 = heapq.heappop(scoville)
        if f1 >= K: return answer
        elif len(scoville) == 0: return -1
        f2 = heapq.heappop(scoville)
        heapq.heappush(scoville, f1 + f2*2)

        answer += 1
