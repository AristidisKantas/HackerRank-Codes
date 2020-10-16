# Score: 100

def solution(A):
    
    if len(A) == 0:
        return 1

    A.sort()

    if A[0] != 1:
            return 1
    if A[len(A)-1] != len(A) + 1:
            return len(A) +1
        
    for i in range(len(A)):
        
        if A[i+1] - A[i] == 2:
            return i+2

#INPUT AND RUN    
test_input = [1,2,3,4,5]
test_run = solution(test_input)
print(test_run)
        