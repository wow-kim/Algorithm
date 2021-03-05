def solution(n, t, m, p):
    
    NOTATION = '0123456789ABCDEF'

    def _decimal(num, base):
        q, r = divmod(num, base)
        n = NOTATION[r]
        if q:
            return _decimal(q, base) + n 
        else:
            return n

    numbers = ""
    answer = ""
    cycle = 0
    num = 0
    p -= 1
    while cycle < t:
        try:
            answer += numbers[cycle*m + p]
            cycle += 1
        except:
            numbers += _decimal(num, n)
            num += 1

    return answer
