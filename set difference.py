# Enter your code here. Read input from STDIN. Print output to STDOUT
nt = int(input())
for _ in range(nt):
    na = int(input())
    a = set(map(int, input().split()))
    nb = int(input())
    b = set(map(int, input().split()))
    c = a.difference(b)
    if len(c) > 0:
        print('False')
    else:
        print('True') 
    