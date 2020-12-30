def solution(pro, spe):
    answer = []
    while len(pro) != 0:
        while pro[0] < 100:
            pro = [i + j for i, j in zip(pro, spe)]
        ans = 0
        for p in pro:
            if p < 100: break
            ans +=1
        answer.append(ans)
        pro = pro[ans:]
        spe = spe[ans:]
        print(pro)
    return(answer)