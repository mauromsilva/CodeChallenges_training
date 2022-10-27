vsentence = 'maro moreira silva'
for c in vsentence:
    vpos = vsentence.find(c)
    vbefore, vafter = '', ''
    vbefore = vsentence[0:vpos]
    vafter = vsentence[vpos+1:]
    vsentence2 = vbefore + vafter
    vpos2 = vsentence2.find(c)
    if vpos2 == -1:
        print(vpos)  
        break