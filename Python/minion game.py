def minion_game(string):
    v=0
    c=0
    for i in range(len(string)):
        if string[i] not in "AEIOU":
            c+=len(string)-i
        else:
            v+=len(string)-i
    if v>c:
        print("Kevin",v)
    elif c>v:
        print("Stuart",c)
    else:
        print("Draw")
