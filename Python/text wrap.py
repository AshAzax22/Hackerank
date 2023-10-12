

def wrap(string, max_width):
    S=""
    i=1
    for j in string:
        S+=j
        if i%max_width==0:
            S+="\n"
        i+=1
    return S

