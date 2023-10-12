from collections import Counter
Sizes=int(input())
SizeAvail=[int(y) for y in input().split()]
SizeCount=Counter(SizeAvail)
#for i in SizeCount:
    #print(i,SizeCount[i])
Income=0
for i in range(int(input())):
    r,m=map(int,list(input().split()))
    for i in SizeCount:
        if i==r:
            if SizeCount[i]>0:
                Income+=m
                SizeCount[i]-=1
print(Income)
