def rotLeft(a, d):
    temp = 0
    for j in range(d):
        for i in range(n):
            if i==0 :
                temp = a[0]
            else:
                a[i-1] = a[i]
        a[n-1] = temp
    
    return a
	
	
def rotLeft(a, d):
    for i in range(d):
        removed = a.pop(0)
        a.append(removed)
    return a