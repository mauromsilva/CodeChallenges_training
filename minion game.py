def minion_game(string):
    # your code goes here
    if len(string) > 0 and len(string) < 10**6:
        vword = ''
        vscorekevin = 0
        vscorestuart = 0
        vwords = []
        for c in string:
            if c not in vwords:
                vwords.append(c)
                if c in 'AEIOU':
                    vscorekevin += string.count(c)
                else:
                    vscorestuart += string.count(c)
                        
        for t in range(2, len(string)): 
            for pos in range(len(string)):
                if t + pos <= len(string): 
                    vword = string[pos:pos+t]
                    if vword not in vwords:
                        vkevin = False
                        vwords.append(vword)
                        if vword[0] in 'AEIOU':
                            vkevin = True
                        vpos = string.find(vword)
                        while vpos != -1:
                            if vkevin:
                                vscorekevin += 1
                            else:
                                vscorestuart += 1
                            vpos = string.find(vword,vpos+1)
                            
        
        if string[0] in 'AEIOU': 
            vscorekevin += 1
        else:
            vscorestuart += 1
                        
        if vscorekevin > vscorestuart:
            print('Kevin ' + str(vscorekevin))
        elif vscorekevin < vscorestuart:
            print('Stuart ' + str(vscorestuart))
        else:
            print('Draw')
             

if __name__ == '__main__':
    s = input()
    minion_game(s)