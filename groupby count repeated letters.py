# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby 
string = input().strip()
groups = ''
vlist = [int(x) for x in string]
for k, g in groupby(vlist):
    groups += '('+str(len(list(g)))+', '+str(k)+') '      
print(groups)
