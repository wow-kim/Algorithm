def solution(n, words):
    before = words[0][0]
    appeared = []

    count = 1
    for w in words:
        if (len(w) == 1) or (before != w[0]) or (w in appeared) :
            break
        before = w[-1]
        appeared.append(w)
        count += 1
        if count == len(words)+1:
            return [0,0]
    num, order = divmod(count,n)
    #몫 -> 차례(order), 나머지 -> 번호(num)
    if order==0:
        order = n
        num = num - 1
    return [order, num+1]