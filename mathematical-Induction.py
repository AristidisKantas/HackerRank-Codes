def count(n):
    result = 0 

    for i in range(n+1):
        result += i

    return result

n = 20
result = count(n)
print(result)