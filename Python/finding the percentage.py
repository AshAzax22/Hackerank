if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        l=student_marks[query_name]
        sum=0
        le=len(l)
        for i in l:
            sum+=i
        avg=sum/le
        print("{0:.2f}".format(avg))
    else:
        print("INVALID INPUT")    
    
