from unittest import result

def isvalid(str) -> bool:
    vcopy = ''
    vchars = {")":"(","}":"{", "]":"["}
    vresult = True
    for c in str:
        if c in '([{':
            vcopy = vcopy + c
        elif c in ')]}':
            if vchars[c] in vcopy[-1:] and len(vcopy)>0:
                vcopy = vcopy[0:-1]
            else:
                vresult = False
                break
    if len(vcopy) > 0:
        vresult = False
    
    return vresult


if isvalid('({{[][][][]{}[]()()}})'):
    print('Valid')
else:
    print('invalid')
