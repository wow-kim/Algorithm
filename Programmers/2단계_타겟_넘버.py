def solution(numbers, target):
    result = []

    def dfs(index, prev):

        value = numbers[index]

        if index == len(numbers)-1:
            result.append(prev+value)
            result.append(prev-value)
            return

        dfs(index + 1, prev+value)
        dfs(index + 1, prev-value)

    dfs(0,0)
    # 더하거나 빼기

    return len(list(filter(lambda x:x==target,result))) # result.count(target)

#------------------------------------------------------

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) \
            + solution(numbers[1:], target+numbers[0])

#------------------------------------------------------

from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)