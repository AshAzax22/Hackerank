def print_formatted(number):
    p=len(bin(number))-2
    for i in range(1,number+1):
        if i//10>0:
            print(" "*(p+1-3),i,end="",sep="")
        else:
            print(" "*(p+1-2),i,end="",sep="")
        if len(oct(i))>3:
            print(" "*(p+1-(len(oct(i))-2)),oct(i)[2:],end="",sep="")
        else:
            print(" "*(p+1-1),oct(i)[2:],end="",sep="")
        if len(hex(i))>3:
            print(" "*(p+1-2),hex(i)[2:].upper(),end="",sep="")
        else:
            print(" "*(p+1-1),hex(i)[2:].upper(),end="",sep="")
        if len(bin(i))>3:
            print(" "*(p+1-(len(bin(i))-2)),bin(i)[2:],sep="")
        else:
            print(" "*(p+1-1),bin(i)[2:],sep="")
        
            

