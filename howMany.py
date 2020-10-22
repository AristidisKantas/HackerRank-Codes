def howMany(s):
    n = len(s)
    index = 0 
    word = ''
    wordList = []
    
    if n == 0: 
        return 0

    while index < n :
        
        while s[index] != ' ' and index < n-1:
            if s[index] != ',' and s[index] != '.' and s[index] != '?' and s[index] != '!' and s[index] >= 'a' and s[index] <= 'z' or s[index] >= 'A' and s[index] <= 'Z':
                word += s[index]
            index += 1
        wordList.append(word)
        word = ''
        index += 1
    
    empty = 0
    for i in wordList:
        if i == '':
            empty += 1
    ans = len(wordList) - empty
    
    return ans

s = 'This is a test. 123 is not-a-word. The result should be 10.'
ans = howMany(s)
print(ans)