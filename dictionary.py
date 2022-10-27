from collections import defaultdict

n, m = map(int, input().strip().split())

A = defaultdict(list)
for i in range(1, n+1):
    A[input()].append(i)

for _ in range (m):
    w = input()
    if A[w]:
        print(*A[w])
    else:
        print(-1) 
