def letterPos(w, x):
    count = 0
    for i in range(0,len(w)):
        if w[i] == x:
            count = i
            return count 
    else:
        return "none"

print(letterPos("alligator", "r"))