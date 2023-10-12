# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
c="H"
if x%2!=0:
    for i in range(x):
        print((c*i).rjust(x-1)+c+(c*i).ljust(x-1))
    for i in range(x+1):
        print((c*x).center(x*2)+(c*x).center(x*6))
for i in range((x+1)//2):
    print((c*x*5).center(x*6))
for i in range(x+1):
    print((c*x).center(x*2)+(c*x).center(x*6))
for i in range(x):
    print(((c*(x-i-1)).rjust(x)+c+(c*(x-i-1)).ljust(x)).rjust(x*6))
