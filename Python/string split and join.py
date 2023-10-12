

def split_and_join(line):
    S=""
    for i in line:
        if i ==" ":
            S+="-"
        else:
            S+=i
    return S
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
