# DADO UM NÚMERO INVERTE ELE
def invertnumber(a):
    charnumber = str(a)
    if charnumber[0] == '-':
        return int('-'+charnumber[:0:-1])
    else:
        return int(charnumber[::-1])

num = input("number: ")
print(invertnumber(num))
