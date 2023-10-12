

# Complete the solve function below.
def solve(s):
    S=s[0].upper()
    for i in range(1,len(s)):
        if s[i-1]==" " :   
            S+=s[i].upper()
        else:
            S+=s[i]
          
    return S
