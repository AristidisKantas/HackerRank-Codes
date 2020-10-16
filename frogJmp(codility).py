# Score: 100

def solution(X, Y, D):
    
    distToTravel = Y - X
    jumpsFloat = distToTravel / D

    jumpsInt = int(jumpsFloat)
    remain = jumpsFloat - jumpsInt
    
    if remain > 0:
        return jumpsInt + 1
    else:
        return jumpsInt
        

#INPUT AND RUN  
x = 1
y = 5
d = 2
temp = solution(x,y,d)
print(temp)