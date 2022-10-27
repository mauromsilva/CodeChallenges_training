# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, n = input().rsplit(' ',1)
r = ["".join(i) for i in permutations(s, int(n))]
r.sort()
for c in r:
    print(c)