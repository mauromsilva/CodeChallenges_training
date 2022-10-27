# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
varray = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

h = sum(1 for i in varray if i in a)
h += sum(-1 for i in varray if i in b)

print(h)
