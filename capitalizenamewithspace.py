#!/bin/python3
import re
# Complete the solve function below.
def solve(s):
    if len(s) > 0 and len(s) < 1000:
        vsep =''
        vlastchar = ''
        vtext = ''
        for c in s: 
            if re.match('^[a-zA-Z]',c):
                if vlastchar.strip() == '':
                    vtext = vtext + c.title()
                else:
                    vtext = vtext + c
            else:
                vtext = vtext + c
            vlastchar = c
    return vtext

print(solve('hello   world  lol'))
print(solve('mauro mor 12silva'))