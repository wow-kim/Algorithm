def solution(n, s):
    if n > s: 
        return [-1]
    a, b = divmod(s, n)
    result = [a]*n

    for i in range(0,b):
        result[i] += 1
    
    return result[::-1]