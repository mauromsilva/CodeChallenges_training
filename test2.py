def morse_codes(vmorsecode):
    vpos = vmorsecode.find('..', 0)
    vcods = []
    # enquanto encontrar ".." não substituido continua a busca a partir da posição de troca inicial
    while vpos != -1:
        # substitui o ".." por "--" 
        if vpos > 0:
            vcods.append(vmorsecode[0:vpos] + '--' + vmorsecode[vpos+3:])
        else:
            vcods.append('--'+vmorsecode[2:])
        
        # enquanto tiver mais um ponto no próximo faz mais um movimento
        if len(vmorsecode) > vpos+1:
            vnextchar = vmorsecode[vpos+1]
        else:
            vnextchar = 'fim'

        while vnextchar == '.':
            vcods.append(vmorsecode[0:vpos+1]+'--'+vmorsecode[vpos+3:])
            vpos += 1
            if len(vmorsecode) > vpos+2:
                vnextchar = vmorsecode[vpos+1]
            else:
                vnextchar = 'fim'

        vpos = vmorsecode.find('..', vpos+1)
    return(vcods)
        
morsecode = '........#..#....'

print(morse_codes(morsecode))