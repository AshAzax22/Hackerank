if __name__ == '__main__':
    l=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    ls=[]
    for i in l:
        if i[1] not in ls:
            ls.append(i[1])
    ls.sort()
   
    z=[x[0] for x in l if x[1] == ls[1] ]
    z.sort()
    for i in z:
        print(i) 
