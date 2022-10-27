from tabnanny import verbose
import re 

def swap_case(s):
    vresult = ''
    for c in s:
        if c == c.upper():
            vresult = vresult + c.lower()
        elif re.match('[a-zA-Z]',c):  
            vresult = vresult + c.upper()
        else:
            vresult = vresult + c
        
    return vresult 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)