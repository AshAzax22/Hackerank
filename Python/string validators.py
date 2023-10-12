if __name__ == '__main__':
    s = input()
    aln=al=num=low=up=False
    for i in  s:
        if i.isalnum():
            aln=True
        if i.isalpha():
            al=True
        if i.isdigit():
            num=True
        if i.islower():
            low=True
        if i.isupper():
            up=True
    print(aln,al,num,low,up,sep="\n")
            
            
        
