def solution(triangle):
    
    i = 1
    while i < len(triangle):
        for j in range(0,i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1] 
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
        i += 1
    return max(triangle[len(triangle)-1])

#------------------------------------------------------
# 메모이제이션
def f(triangle, i, j, memo):
    if i == len(triangle)-1:
        return triangle[i][j]

    if (i,j) in memo:
        return memo[(i,j)]

    a = f(triangle, i+1, j, memo)
    b = f(triangle, i+1, j+1, memo)
    x = triangle[i][j] + max(a, b)

    memo[(i,j)] = x

    return x

def solution(triangle):
    memo = {}
    answer = f(triangle, 0, 0, memo)
    return answer

