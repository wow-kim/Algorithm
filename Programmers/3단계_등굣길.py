# 시간 초과
def solution1(m, n, puddles): 
    
    # 재귀
    def recur(i=1, j=1):
        if [i,j] == [m,n]:
            return 1
        
        if [i,j] in puddles:
            return 0
        
        if (i == m) & (j != n):
            return recur(i, j+1)
        
        if (i !=m ) & (j == n):
            return recur(i+1, j)
        
        return recur(i+1, j) + recur(i, j+1)
    
    answer = recur(1,1) % 1000000007
    return answer


