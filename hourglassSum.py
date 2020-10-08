def hourglassSum(arr):

    sumArray = [0]*16
    j = i = t = 0
    arrayLength = len(arr) - 1 #5
    
    for i in range(arrayLength-1):
        for j in range(arrayLength-1):
            sumArray[t] = arr[i][j] + arr[i][j+1] +arr[i][j+2] +arr[i+1][j+1] +arr[i+2][j] +arr[i+2][j+1] +arr[i+2][j+2]
            t += 1
    return max(sumArray) 