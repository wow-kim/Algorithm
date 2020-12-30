def solution(w,h):
    # 최대공약수와 최소공배수 이용
    
    number = max(w, h)
    divisor = min(w, h)
    
    while (number % divisor) != 0:
        remainder = number % divisor
        
        number = divisor
        divisor = remainder
    
    x = w/divisor
    y = h/divisor
    
    answer = w*h - (x+y-1)*divisor
    
    return answer