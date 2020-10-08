def repeatedString(s, n):
    bigStringWithoutLetters = ""
    a_counter = 0
    a_remaining_counter = 0
    total_a_counter = 0
    if n > pow(10,12) or n < 1: 
        return "Error in n input"

    if len(s) > 100 or len(s) < 1 :
        return "Error in s input"

    timesWhole = n//len(s)
    lettersRemaining = n - timesWhole*len(s)
    lettersAdded = timesWhole*len(s)

    for i in range(len(s)):
        if s[i] == "a":
            a_counter += 1

    if n%len(s) == 0:
        total_a_counter = a_counter*timesWhole
    else: 
        for i in range(lettersRemaining):
            if s[i] == "a":
                a_remaining_counter += 1
        total_a_counter = a_counter*timesWhole + a_remaining_counter

    return total_a_counter