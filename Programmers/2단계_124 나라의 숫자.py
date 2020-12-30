def solution(n):
    l = 1
    while n - 3**l > 0 :
        n -= 3**l 
        l += 1

    n = n-1
    l = l-1
    answer = []
    while l > 0:
        d, n = divmod(n,3**l) 
        if d==2:
            answer.append(d+2)
        else:
            answer.append(d+1)
        l -= 1
    if n==2:
        answer.append(4)
    else:
        answer.append(n+1)
    answer = [str(i) for i in answer]
    return "".join(answer)