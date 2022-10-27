mc = '...........-..-'
result = []
i = 0
while i < len(mc):
    pos = mc.find('..', i) 
    if  pos != -1:
        result.append(mc[:pos] + mc[pos:].replace('..','--',1))
        i = pos + 2
    else:
        i = len(mc)

print(result)
        