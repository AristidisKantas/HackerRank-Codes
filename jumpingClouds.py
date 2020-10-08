def jumpingOnClouds(c):
    
    listLength = len(c)
    clouds = listLength - 1
    jump = 0 
    i = 0
    end = False

    while i <= clouds:
        
        if i >= clouds:
            break
        if i + 2 <= clouds:
            if c[i + 2] == 0: 
                jump += 1
                i = i + 2
            elif c[i + 1] == 0:
                i += 1
                jump += 1
        elif i + 1 <= clouds:
            if c[i + 1] == 0:
                i += 1
                jump += 1
            
    return jump