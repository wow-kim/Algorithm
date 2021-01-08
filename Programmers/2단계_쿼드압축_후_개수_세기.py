def solution(arr):
    
    answer = [0,0]
    
    def recursive(arr):
        n = len(arr)
        
        cut_0 = lambda x : x[0:int(n/2)]
        cut_n = lambda x : x[int(n/2):n]
        
        zero = 0
        one = 0
        for a in arr:
            zero += a.count(0)
            one += a.count(1)
        
        if one == 0:
            answer[0] = answer[0] + 1
        elif zero == 0:
            answer[1] = answer[1] + 1
        else:
            recursive(list(map(cut_0,arr[0:int(n/2)])))
            recursive(list(map(cut_n,arr[0:int(n/2)])))
            recursive(list(map(cut_0,arr[int(n/2):n])))
            recursive(list(map(cut_n,arr[int(n/2):n])))
            
    recursive(arr)
    
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))