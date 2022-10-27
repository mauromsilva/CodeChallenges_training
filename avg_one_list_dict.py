if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))

        student_marks[name] = scores
    
    query_name = input()

if n >= 2 and n <= 10:
    vscor = student_marks[query_name]
    vavg = sum(vscor)/len(vscor)
    print("{:.2f}".format(vavg))

    