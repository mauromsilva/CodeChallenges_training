def invertern(a):
    chara = str(a)
#    print(chara[::-1])
#    print(chara[-2])
#    print(chara[-3])

    if chara[0] == '-':
        chara = chara[0] + chara[:0:-1]
    else:
        chara = chara[::-1]
    return(chara)

vnum = input("Number ")
print(invertern(vnum))
