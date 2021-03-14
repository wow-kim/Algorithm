# 시간 초과 -> 중복계산때문인듯
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

# 시간 초과 해결
def solution(m, n, puddles):
    answers=[[0]*(m+1) for i in range(n+1)]
    answers[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            if [j,i] in puddles:
                answers[i][j]=0
            else:
                answers[i][j]=answers[i-1][j]+answers[i][j-1]
    return answers[n][m]%1000000007

