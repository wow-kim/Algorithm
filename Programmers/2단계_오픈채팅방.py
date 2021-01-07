def solution(record):
    record = list(map(lambda x: x.split(" "), record))

    id_nickname = {}
    log = []

    for r in record:
        if r[0] == "Enter":
            id_nickname[r[1]] = r[2]
            log.append([r[1],"님이 들어왔습니다."])
        elif r[0] == "Leave":
            log.append([r[1],"님이 나갔습니다."])
        else:
            id_nickname[r[1]] = r[2]

    def change(l):
        nick = id_nickname[l[0]]
        return nick+l[1]

    return list(map(change, log))
