def solution(dirs):
    walk = []
    location = [0,0]
    for dir in dirs:
        if dir == "U" and location[1] != 5:
            to = [i+j for i,j in zip(location, [0,1])]
        elif dir == "D" and location[1] != -5:
            to = [i+j for i,j in zip(location, [0,-1])]
        elif dir == "L" and location[0] != -5:
            to = [i+j for i,j in zip(location, [-1,0])]
        elif dir == "R" and location[0] != 5:
            to = [i+j for i,j in zip(location, [1,0])]
        else:
            continue
        walk.append([location, to])
        location = to

    walk = list(map(lambda x: sorted(x), walk))

    answer = []
    for w in walk:
        if w not in answer:
            answer.append(w)
    return len(answer)
