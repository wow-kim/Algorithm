import collections
def solution(n, results):

    over = collections.defaultdict(set)
    under = collections.defaultdict(set)

    for a, b in results:
        under[a].add(b)
        over[b].add(a)

    for player in range(1, n+1):
        # over
        for i in under[player]:
            over[i].update(over[player])

        # under
        for j in over[player]:
            under[j].update(under[player])

    answer = 0
    for i in range(1, n+1):
        if len(over[i]) + len(under[i]) == n-1:
            answer += 1

    return answer