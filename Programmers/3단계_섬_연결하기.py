def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    nodes = [costs[0][0]]
    while len(nodes) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in nodes) and (cost[1] in nodes): continue
            if (cost[0] in nodes) or (cost[1] in nodes):
                answer += cost[2]
                nodes.append(cost[0])
                nodes.append(cost[1])
                nodes = list(set(nodes))
                costs.pop(i)
                break
    return answer