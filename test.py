morsecode = '....#..#....#ask'
morsecode = '........#..#....'
vlist = []
for i in range(len(morsecode)-1):
    if morsecode[i]+morsecode[i+1] == '..' :
        vlist.append(morsecode[:i] + '--' + morsecode[i+2:])
print(vlist)