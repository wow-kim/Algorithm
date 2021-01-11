def solution(n,a,b):
    
    a, b = a-1, b-1

    answer = 1
    while a // 2 != b // 2:
        answer += 1
        a = a // 2
        b = b // 2

    return answer

#----------------------------

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()