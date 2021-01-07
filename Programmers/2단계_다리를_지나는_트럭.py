def solution(bridge_length, weight, truck_weights):
    
    land = []
    bridge = []
    ready = []
    
    def move(bridge):
        for b in range(len(bridge)):
            bridge[b][1] = bridge[b][1]-1
        return bridge
    
    for t in truck_weights:
        land.append([t,bridge_length])
    bridge.append(land.pop(0))
    bridge = move(bridge)
    
    time = 1
    
    while land != [] or bridge !=[]:
        
        bridge = move(bridge)
        
        if ready == [] and land != [ ]:
            ready.append(land.pop(0))
        
        if bridge[0][1] == -1:
            bridge = bridge[1:]
        
        if sum([i for i,j in bridge+ready]) <= weight and ready != [ ]:
            ready = move(ready)
            bridge.append(ready.pop(0))
        
        time += 1
        
    return time