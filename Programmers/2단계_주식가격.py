def solution(prices):
    ans=[]
    for i in range(len(prices)):
        count = 0
        a= prices[i]
        for j in range(i+1,len(prices)):
            if prices[j] >= a:
                count +=1
            else:
                count+=1
                ans.append(count)
                break
            if j == (len(prices) - 1) :
                ans.append(count)

    ans.append(0)
    return ans