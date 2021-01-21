import heapq
def solution(operations):
    answer = []
    for op in operations:
        op1, op2 = op.split(" ")
        if op1 == "I":
            heapq.heappush(answer, int(op2))
        elif answer:
            if op2 == "1":
                answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
            else:
                heapq.heappop(answer)
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0,0]