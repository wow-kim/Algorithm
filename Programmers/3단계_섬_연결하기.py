import collections
def solution(n, costs):
    graph = collections.defaultdict(list)
    for a, b, cost in costs:
        graph[a].append([b,cost])
    
    def to_final(node, visited = [], cost_sum = 0, answer = float("Inf")):
        print(node, visited, cost_sum, answer)
        if not graph[node]:
            if sorted(visited) == sorted(list(range(n))):
                answer = min(answer, cost_sum)
                return answer
            else:
                return answer
        else:
            for next_node, cost in graph[node]:
                cost_sum += cost
                answer = to_final(next_node, visited + [node] , cost_sum)
                print(answer)
    
    result = []
    for i in range(n):
        result.append(to_final(i))
    
    return result

answer = solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
print(answer)