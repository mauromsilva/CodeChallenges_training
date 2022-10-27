# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
c = a.intersection(b)
result = set(i for i in a if i not in c)
result = result.union(set(i for i in b if i not in c))

for c in sorted(result):
    print(c)
