import numbers

#set 1...n
#1 duplicated and lost one number (find them)
varray = [1,2,3,4,3]
varray = [1,2,2]
vret = []
for ind, number in enumerate(varray, 1):
    if ind != number:
        vret.append(number)
        vret.append(ind)
print(vret)
