import datetime
def solution(m, musicinfos):

    melody = []
    for c in m:
        if c == '#':
            melody.append(melody.pop() + c)
        else:
            melody.append(c)

    def find_index(data, target):
        res = []
        lis = data
        while True:
            try:
                res.append(lis.index(target) + (res[-1]+1 if len(res)!=0 else 0)) 
                lis = data[res[-1]+1:]
            except:
                break     
        return res

    def findMusic(music):
        start, end, name, sound = music.split(",")

        t1 = datetime.datetime.strptime(start, '%H:%M')
        t2 = datetime.datetime.strptime(end, '%H:%M')
        term = ((t2 - t1).seconds) // 60

        radio = []
        for s in sound:
            if s == '#':
                radio.append(radio.pop() + s)
            else:
                radio.append(s)

        try:
            res = find_index(radio, melody[0])
        except:
            return False

        for i in res:
            t = i
            cur = 0
            while t < term :
                if i == len(radio):
                    i = 0

                if radio[i] == melody[cur]:
                    cur += 1
                else:
                    cur = 0

                i += 1
                t += 1

                if cur == len(melody):
                    return [term, start, name]

        return False

    results = []
    for mus in musicinfos:
        ans = findMusic(mus)
        if ans:
            results.append(ans)

    results = sorted(results, key=lambda x: (-x[0], x[1]))

    if results:
        return results[0][2]
    else:
        return '(None)'