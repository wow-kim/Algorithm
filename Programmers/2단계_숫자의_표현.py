def solution(n):
    result = 0

    i = 1
    while i*(i+1)/2 <= n:
        i += 1
    max_count = i - 1
    
    while max_count > 0:
        if max_count % 2 != 0 :
            mid = n / max_count
        else:
            mid = n / max_count - 1/2
            
        if mid == int(mid):
            result += 1
            
        max_count -= 1
        
    return result