def solution(n):
    
    triangle = [[0]*i for i in range(1,n+1)]

    i, j = 0, 0

    side_now = 'left'
    to = n
    for num in range(1, sum(range(1,n+1))+1):
        triangle[j][i] = num
        if side_now == 'left':
            if num == to:
                side_now = 'bottom'
                n -= 1
                to += n
                i += 1
            else:
                j += 1
        elif side_now == 'bottom':
            if num == to:
                side_now = 'right'
                n -= 1
                to += n
                i -= 1
                j -= 1
            else:
                i += 1
        elif side_now == 'right':
            if num == to:
                side_now = 'left'
                n -= 1
                to += n
                j += 1
            else:
                i -= 1
                j -= 1

    answer = []
    for tri in triangle:
        answer.extend(tri)

    return answer