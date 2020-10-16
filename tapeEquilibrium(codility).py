# Score : 50 O(n^2)

def solution(A):
    left_sum = right_sum = min_diff = diff = 0
    for p in range(1, len(A)):
        for i in range(0,p):
            left_sum += A[i]
        for j in range(p, len(A)):
            right_sum += A[j]
        
        diff = abs(left_sum - right_sum)
        if p == 1:
            min_diff = diff
        left_sum = right_sum = 0
        if diff < min_diff:
            min_diff = diff
            
    return min_diff

# Score : 100 O(n)
def solution(A):          
    s = sum(A)
    m = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        m = min(abs(s - 2*left_sum), m)
    return m