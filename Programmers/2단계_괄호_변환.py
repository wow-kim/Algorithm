def IsCorrect(string):
        pa = {'(':0, ')':0}
        for s in string:
            pa[s] = pa[s] + 1
            if pa[')'] > pa['(']: return False
        if pa[')'] != pa['(']: return False
        return True

def solution(p):
    if p == '':
        return ''

    par = { '(':0, ')':0 }
    u = p[0]
    p = p[1:]
    par[u] = 1
    while par['('] != par[')']:
        e = p[0]
        p = p[1:]
        u += e
        par[e] = par[e] + 1
    v = p

    if IsCorrect(u):
        answer = u + solution(v)
        return answer

    else:
        temp = "("
        temp = temp + solution(v)
        temp = temp + ")"

        answer = ""
        for w in u[1:-1]:
            if w == ")": answer += "("
            else: answer += ")"

        return temp + answer

print(solution(")("))
print(solution("()))((()"))