from gettext import find

def avgwordlength(psentence):
    vremainsentence = psentence
    vlenwords = []
    while vremainsentence:
        if vremainsentence.find(' ') == -1:
            vword = vremainsentence
            vremainsentence = ''
        else:
           vword = vremainsentence[:vremainsentence.find(' ')]
           vremainsentence = vremainsentence[vremainsentence.find(' ')+1:]
        vlenwords.append(len(vword))
    
    vsum = 0
    vcont = 0
    for c in vlenwords:
        vsum = c + vsum
        vcont = vcont + 1

    return(vsum/vcont)

vsentence = input("Sentence: ")
print(avgwordlength(vsentence))