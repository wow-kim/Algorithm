import collections
def solution(n, k):

    def fac(n):
        dp = collections.defaultdict(int)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]*i
        return dp[n]   

    people = [i for i in range(1,n+1)]
    answer = []

    while n > 0:
        ind = fac(n) // n 
        i, k = divmod(k, ind)
        if k == 0:
            answer.append(people.pop(i-1))
        else:
            answer.append(people.pop(i))  
        n -= 1

    return answer