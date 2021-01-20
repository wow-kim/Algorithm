import collections
def solution(genres, plays):
    dic = collections.defaultdict(list)
    for i, x in enumerate(zip(genres, plays)):
        dic[x[0]].append((x[1],i))

    keys = sorted(dic.keys(), key=lambda x: -sum(d[0] for d in dic[x]))

    answer = []
    for key in keys:
        song = dic[key]
        song = sorted(song, key=lambda x: (-x[0], x[1]))
        if len(song) >= 2:
            song = song[:2]

        answer.extend([x[1] for x in song])

    return answer
