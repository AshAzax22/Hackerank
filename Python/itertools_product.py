from itertools import product
l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
l=list(product(l1,l2))
for i in l:
    print(i,end=" ")
