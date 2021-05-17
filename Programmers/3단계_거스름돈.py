# 큐를 이용한 풀이, 효율성 X
from collections import deque
def solution1(n, money):
    
    answer = 0
    money = set(money)
    dic = {}
    for m in money:
        dic[m] = 0
    
    queue = deque()
    queue.append((n, money, dic))
    visited = []
    while queue:
        leaving, coins, memo = queue.popleft()
        if leaving == 0:
            if memo not in visited:
                answer += 1
                visited.append(memo)
                continue
        
        if min(coins) > leaving:
            continue
        
        for coin in coins:
            if coin > leaving:
                continue
                
            for i in range(1, leaving // coin + 1):
                l = leaving - coin*i
                temp = memo.copy()
                temp[coin] += i
                queue.append((l, coins-set([coin]), temp))
        
    return answer

# 다른 사람의 풀이, 현타온다
from collections import defaultdict
def solution(n, money):
    dp=defaultdict(int)   
    dp[0]=1

    for m in money:
        for i in range(m,n+1):
            dp[i]+=dp[i-m]%1000000007
    return dp[n]