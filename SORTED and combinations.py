# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

string, n = input().rsplit(' ',1)
n = int(n)

for i in range(1,n+1):
    vlist = list(combinations(sorted(string),i))
    for c in vlist:
         print("".join(c))