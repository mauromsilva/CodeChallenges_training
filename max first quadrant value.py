a = []
a.append(list(map(int, '112 42 83 119'.split(' '))))
a.append(list(map(int, '56 125 56 49'.split(' '))))
a.append(list(map(int, '15 78 101 43'.split(' '))))
a.append(list(map(int, '62 98 114 108'.split(' '))))

n = len(a)
sum = 0
for i in range(n//2): # line
    for j in range(n/2):
        sum += max(a[i][j], a[i][n-j-1],  a[n-i-1][j], a[n-i-1][n-j-1])

print(sum)