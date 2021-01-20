def solution(routes):
    cameras = []
    sta = routes[0][0]
    fin = routes[0][1]
    
    for a, b in sorted(routes):
        if fin < a:
            cameras.append([sta,fin])
            sta = a
            fin = b
        else:
            sta = max(sta, a)
            fin = min(fin, b)
            
    cameras.append([sta,fin])      
    return len(cameras)