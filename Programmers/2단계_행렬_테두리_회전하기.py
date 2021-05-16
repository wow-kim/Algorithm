def solution(rows, columns, queries):
    table = [[columns*(i-1) + j for j in range(1, columns+1)] for i in range(1, rows+1)]
    answer = []

    for x1, y1, x2, y2 in queries:
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -=1
        temp = {}

        for y in range(y1, y2):
            temp[(x1, y+1)] = table[x1][y]
        for x in range(x1, x2):
            temp[(x+1, y2)] = table[x][y2]
        for y in range(y2, y1, -1):
            temp[(x2, y-1)] = table[x2][y]
        for x in range(x2, x1, -1):
            temp[(x-1, y1)] = table[x][y1]

        answer.append( min(temp.values()) )
        for key, value in temp.items():
            x, y = key
            table[x][y] = value

    return answer