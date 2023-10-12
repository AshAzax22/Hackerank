# Enter your code here. Read input from STDIN. Print output to STDOUT
def score_words():
    x=int(input())
    s=input().split()
    score=0
    for i in s:
        c=0
        for j in i:
            if j in "aeiouy":
                c+=1
        if c%2==0:
            score+=2
        else:
            score+=1
    print(score)
score_words()
