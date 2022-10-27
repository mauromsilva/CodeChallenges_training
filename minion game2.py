def subs(string, ret=['']):
    if len(string) == 0:
        return ret
    head, tail = string[0], string[1:]
    ret = ret + list(map(lambda x: x+head, ret))
    return subs(tail, ret)

def minion_game(string):
    # your code goes here
    if len(string) > 0 and len(string) < 10**6:
        vscorekevin = 0
        vscorestuart = 0
        words = []
        length = len(string)
        #for vtam in range(1,length+1):
        words = subs(string)
        words.remove('')
        dicwords = dict.fromkeys(words)
        for c in dicwords:
            count = words.count(c)
            vkevin = False
            if c[0] in 'AEIOU':
                vkevin = True
            if vkevin:
                vscorekevin += count
            else:
                vscorestuart += count
#            words = []
#            dicwords = {}
                                        
                            
        if vscorekevin > vscorestuart:
            print('Kevin ' + str(vscorekevin))
        elif vscorekevin < vscorestuart:
            print('Stuart ' + str(vscorestuart))
        else:
            print('Draw')             

if __name__ == '__main__':
    s = input()
    minion_game(s)