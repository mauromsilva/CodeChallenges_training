#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
def sort_key(list):
    return list[1]

if __name__ == '__main__':
    s = input()
    listcounter = Counter(sorted(s)).most_common(3)

    for key, value in listcounter:
        print(key, value)

