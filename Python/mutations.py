def mutate_string(string, position, character):
    c=0
    s=""
    for i in string:
        if c==position:
            s+=character
            c+=1
        else:
            s+=i
            c+=1
    return s

