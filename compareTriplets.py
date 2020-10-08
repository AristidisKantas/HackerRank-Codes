def compareTriplets(a, b):
    points_A = 0
    points_B = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            points_A = points_A + 1
        elif a[i] < b[i]:
            points_B = points_B +1
        
    return (points_A,points_B)
  