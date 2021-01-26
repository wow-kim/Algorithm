import collections
import itertools
def solution(orders, course):

    result = []
    for c in course:
        dic = {}
        for order in orders:
            for x in list(map(lambda x: "".join(sorted(list(x))), itertools.combinations(order, c))):
                dic[x] = dic.get(x, 0) + 1 

        if dic.values():
            max_c = max(list(dic.values()))

        if max_c >= 2:
            for k, v in dic.items():
                if v == max_c:
                    result.append(k)

    return sorted(result)