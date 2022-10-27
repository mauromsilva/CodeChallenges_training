from os import remove


if __name__ == '__main__':
    N = int(input())

voper = ''
vcopy = []
vlist = []
vlistprint = []
for i in range(N):
    voper = input()
    if voper.find(' ') != -1:
        voper, *velem = voper.split()
        velements = list(velem)
    if voper == 'insert':
        vlist.insert(int(velements[0]), int(velements[1]))
    elif voper == 'remove':
        vlist.remove(int(velements[0]))
    elif voper == 'print':
        vcopy = vlist[:]
        vlistprint.append(vcopy)
    elif voper == 'append':
        vlist.append(int(velements[0]))
    elif voper == 'sort':
        vlist.sort()
    elif voper == 'pop':
        vlist.pop()
    elif voper == 'reverse':
        vlist.reverse()
    
for c in vlistprint:
    print(c)