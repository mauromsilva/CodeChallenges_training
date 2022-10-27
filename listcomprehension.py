
# Create axis
x = 2
y = 2
z = 2
n=2
vcube = []
for xp in range(0,x+1):
    for yp in range(0, y+1):
        for zp in range(0, z+1):
            if xp + yp + zp != n:
                vcube.append([xp, yp, zp])
            
vcube.sort()
print(vcube)