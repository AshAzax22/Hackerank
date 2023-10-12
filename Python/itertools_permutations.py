# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
l=[x for x in input().split()]
x=[y for  y in permutations(l[0],int(l[1]))]
s=[]
for i in x:
    t=""
    for j in i:
         t+=j
    s.append(t)
s.sort()
for i in s:
    print(i)
