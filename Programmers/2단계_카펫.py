def solution(brown, yellow):
    
    m = 3
    while m < 2500:
        if yellow % (m-2) == 0:
            n = -m + 2 + brown/2
            if (m-2)*(n-2) == yellow:
                return(sorted([m,n],reverse=True))
        m += 1
        
print(solution(10,2))
print(solution(8,1))
print(solution(24,24))