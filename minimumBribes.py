def minimumBribes(q):
    
    numberOfQueues = q[0]
    bribes = 0
    arrayLength = len(q) - 1
    chaos = False

    q = [element - 1 for element in q]

    for i in range(arrayLength,-1,-1):
        if i - q[i] < -2:
            chaos = True
        for j in range(i-1, -1,-1):
            if q[j] > q[i]:
                bribes += 1
            
    #for i in range(arrayLength):
        #if i - q[i] < 0 and i - q[i] >= -2 :
            #bribes = bribes + abs(i - q[i]) 
        #elif i - q[i] >= 3:
            #bribes = bribes + 1    
        #elif i - q[i] < -2:
            #chaos = True
        
    if chaos:
        print('Too chaotic')
    else:
        print(bribes)