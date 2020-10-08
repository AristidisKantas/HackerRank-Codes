def diagonalDifference(arr):
    
    
    length = len(arr[0])
    
    y = len(arr[0])
    sumLD = 0
    sumRD = 0

    for i in range(length):
        sumLD += arr[i][i] 
        y = y - 1
        sumRD += arr[y][i] 
        
    return abs(sumLD - sumRD)