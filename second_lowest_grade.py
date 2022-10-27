if __name__ == '__main__':
    vrecords = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        vrecords.append((name, score))

    vfirst  = None
    vsecname = None
    vsecscore = None
    vlows = []
    from operator import itemgetter
    for (vname, vscore) in sorted(vrecords, key = itemgetter(1)):
        if vfirst == None:
            vfirst = vscore
        else:
            if (vsecscore == None) and (vscore != vfirst):
                vsecscore = vscore
                vsecname = vname
            if vscore == vsecscore: 
                vlows.append((vname,vscore))

    for vname in sorted(vlows):
        print(vname[0])

