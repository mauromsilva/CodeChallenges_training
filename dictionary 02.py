# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
d = OrderedDict()
for _ in range(n):
    name, price = input().rsplit(' ',1)
    if name in d:
        d[name] += int(price) 
    else:
        d[name] = int(price) 
        

for c in d:
    print(c, d[c])