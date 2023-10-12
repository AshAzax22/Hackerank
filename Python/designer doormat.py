# Enter your code here. Read input from STDIN. Print output to STDOUT
x=[int(y) for y in input().split()]
if x[0]%2!=0 and x[0]*3==x[1]:
    for i in range(0,x[0]//2):
        print("-"*(x[1]//2-1-(3*i)),".|."*(i*2+1),"-"*(x[1]//2-1-(3*i)),sep="")
    print("-"*((x[1]-7)//2),"WELCOME","-"*((x[1]-7)//2),sep="")
    for i in range(0,x[0]//2):
        print("-"*(3+3*i),".|."*(x[0]-(2*i+2)),"-"*(3+3*i),sep="")
