def sockMerchant(n, ar):
    pair = 0 
    
    for element in set(ar):
        pair += ar.count(element) // 2

    return pair
