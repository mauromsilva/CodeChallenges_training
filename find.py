string = 'mauro moreira silva  mauro silva'
substring = 'mauro'
vpos = 0
vcont = 0
while vpos != -1:
    vpos = string.find(substring, vpos)
    if vpos != -1:
        vcont = vcont + 1
        vpos = vpos+len(substring)+1
    
print(vcont)

