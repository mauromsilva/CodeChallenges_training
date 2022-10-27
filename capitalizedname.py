#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    vresult = s.split()
    vtext = ''
    vsep =''
    if len(s) > 0 and len(s) < 1000:
        for word in vresult:
            if re.match('^[a-zA-Z]',word[0]):  
                s.find()
                vtext = vtext + vsep + word.title()
                vsep = ' '
            else:
                vtext = vtext + ' ' + word
    return vtext

print(solve('hello   world  lol'))

for c in 'hello   world  lol':
    print(c)