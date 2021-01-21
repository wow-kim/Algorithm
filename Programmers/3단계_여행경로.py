import collections
def solution(tickets):
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    path = []
    def dfs(ap):
        while graph[ap]:
            dfs(graph[ap].pop(0))
        path.append(ap)
        
    dfs("ICN")
    
    return path[::-1]