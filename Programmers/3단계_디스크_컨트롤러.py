import heapq
def solution(jobs):
    N = len(jobs)
    jobs = sorted(jobs)

    now = 0
    answer = 0
    ready = []

    while jobs or ready:
        while jobs and jobs[0][0] <= now:
            heapq.heappush(ready ,jobs.pop(0)[::-1])

        if ready:
            job = heapq.heappop(ready)
            now += job[0]
            answer += now - job[1]
        else:
            now += 1

    return answer // N