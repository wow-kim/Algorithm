def solution(files):
        
    file_spl = []
    for i, file in enumerate(files):
        
        file = list(file)
        
        head = []
        while not file[0].isdigit():
            head.append(file.pop(0))
        
        number = []
        while file[0].isdigit() and len(number) < 5:
            number.append(file.pop(0))
            if not file:
                break
        
        head = "".join(head)
        number = "".join(number)
        
        if file:
            tail = "".join(file)
        else:
            tail = ""
            
        file_spl.append((head, number, tail, i))
    
    file_spl = sorted(file_spl, 
                      key=lambda x: (x[0].upper(), int(x[1]), x[3]))
    def assemble(x):
        return x[0]+x[1]+x[2]
    
    return list(map(assemble, file_spl))