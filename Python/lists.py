if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        x=[i for i in input().split()]
        if x[0]=="insert":
            l.insert(int(x[1]),int(x[2]))
            continue
        elif x[0]=="print":
            print(l)
            continue
        elif x[0]=="remove":
            if int(x[1]) in l:
                l.remove(int(x[1]))     
            continue
        elif x[0]=="append":
            l.append(int(x[1]))
            continue
        elif x[0]=="sort":
            l.sort()
            continue
        elif x[0]=="pop":
            l.pop()
            continue
        elif x[0]=="reverse":
            l.reverse()
            continue
        else:
            print("invalid input")
            i-=1
