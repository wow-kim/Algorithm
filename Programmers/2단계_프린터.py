def solution(priorities, location):
    
    prior_set = sorted(list(set(priorities)), reverse=True)
    priorities = [[i,j] for i,j in enumerate(priorities)]
    count = 0

    for i in prior_set:
        front = []
        back = []
        for p in priorities:
            if p[1] == i:
                back = back + front
                front = []
                count += 1
                if p[0] == location:
                    return count
            else:
                front.append(p)
        priorities = front + back