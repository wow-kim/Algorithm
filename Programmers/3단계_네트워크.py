def solution(n, computers):
    
    answer = 0
    bfs = []
    visited = [0]*n

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1

        while bfs:
            node = bfs.pop(0)
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer