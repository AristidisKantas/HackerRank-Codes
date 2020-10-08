def countingValleys(steps, path):
    levelArr = [0]*steps
    level = 0
    isInValley = False
    valleyCounter = 0
    
    for i in range(steps):
        if path[i] == 'U':
            level += 1
        elif path[i] == 'D':
            level -= 1
        levelArr[i] = level
        
    for j in range(len(levelArr)):
        if levelArr[j] < 0 and isInValley == False:
            isInValley = True
        if levelArr[j] == 0 and isInValley == True:
            valleyCounter += 1
            isInValley = False
    return valleyCounter
    