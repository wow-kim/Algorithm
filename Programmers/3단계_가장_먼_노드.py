# BFS
import collections
def solution(n, edge):

    short = [0]*(n+1)
    graph = collections.defaultdict(set)
    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)

    visited = set([1])
    nodes = [1]
    dist = 0
    while len(visited) < n:
        visited.update(nodes)
        temp = set()
        while nodes:
            node = nodes.pop()
            short[node] = dist

            for next in graph[node] - visited :
                temp.add(next)
            #print(temp)
        nodes = temp
        dist += 1

    return short.count(max(short))