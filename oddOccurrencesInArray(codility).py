# Score: 66

def solution(A):
    if len(A) == 1:
        return A[0]
        
    if len(A) == 0:
        return 0
        
    arr_length = len(A)
    
    i = 1
    j = 0
    temp = 0
    iter_length = arr_length
    
    while temp < iter_length:
        if A[0] == A[i]:
            A.pop(0)
            A.pop(i-1)
            iter_length -= 2
            temp = i = 1
        else:
            i += 1
            temp += 1
            
    unpaired  = A[0]
    return unpaired


#INPUT AND RUN :