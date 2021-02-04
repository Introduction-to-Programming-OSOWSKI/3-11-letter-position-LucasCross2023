def letterPos(w):
    count = 0
    for i in range(len(w)):
        if w[i] == "n":
            count = i
    
    return count 

print(letterPos("sunshine"))