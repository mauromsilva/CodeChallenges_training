if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

vvalid = True
varr = list(arr)

if n >= 2 and n <= 10:
    for c in varr:
        if c < -100 and c > 100:
            vvalid = False
    if vvalid:
        vsorted = sorted(varr, reverse=True)
        vult = None 

        for c in vsorted:
            if vult == None:
                vult = c
            else:
                if c < vult:
                    vup = c
                    break
                vult = c
        print(vup)