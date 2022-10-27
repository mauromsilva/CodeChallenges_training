#varray = [5,3,2,1]
#varray = [6,5,4,4]
#varray = [1,1,1,3,3,4,3,2,4,2]
varray = [1,1,2,3,7]
vdifference = 0
vindex = 0

vmonotonic = True 

for c in varray:
    if vindex +1 < len(varray) and vindex > 0:
        
        vdifference = varray[vindex+1] - varray[vindex]

        if (vdifference >= 0 and varray[vindex-1] >  varray[vindex]) or (vdifference < 0 and varray[vindex-1] <  varray[vindex]):
            vmonotonic = False
            break
    vindex += 1

if vmonotonic:
    print('é monotonico')
else:
    print('não é monot')


