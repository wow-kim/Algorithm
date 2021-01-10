def solution(n):
    count = 0
    while(n>0):
        d,m = divmod(n,2)
        if m == 1 : count += 1
        n = d
    return count

#-------------------------------

def solution(n):
    return bin(n).count('1')