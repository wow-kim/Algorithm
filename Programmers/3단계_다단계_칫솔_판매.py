import math

def solution(enroll, referral, seller, amount):
    # 이익을 저장하는 dict
    profit = {}
    for e in enroll:
        profit[e] = 0
        
    # 조직 구조를 저장하는 dict
    tree = {}        
    for i, r in enumerate(referral):
        if r == '-':
            tree[enroll[i]] = 'center'
        else:
            tree[enroll[i]] = r
    
    # 상위 노드로 올라가면서 계산 
    for i in range(len(seller)):
        p, money = seller[i], amount[i]*100
        
        while p != 'center':
            pay = math.floor(money / 10)
            mine = money - pay
            profit[p] += mine
            
            p = tree[p]
            money = pay
        
    return list(profit.values())