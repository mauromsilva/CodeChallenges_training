from msilib.schema import _Validation_records


def print_rangoli(size):
    # your code goes here
    vword = ''
    vletter = ''
    vlast = ''
    vspace = ''
    for c in range(size):
        vword = vword + vspace + chr(97 + c)
        vspace = '-'
    vword = vword[::-1] + vword[1:]
    vwidth = len(vword)
    
    vlist = []

    for c in range(size-1):
        vletter = chr(96 + size - c)
        vtext = vlast[::-1] + '-' + vletter + '-' + vlast 
        vlast = vtext[vtext.find(vletter):].strip()
        vlist.append(vtext.center(vwidth, '-'))
        print(vtext.center(vwidth, '-'))
    print(vword)

    vlist = vlist[::-1]
    for c in vlist:
        print(c)

if __name__ == '__main__':
    print_rangoli(13)