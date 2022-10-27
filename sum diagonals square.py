# soma diagonais do quadrado
arr = []
arr.append([1, 3, 9])
arr.append([1, 2, 3])
arr.append([1, 5, 0])

vallr = 0
valrl = 0 
for i in range(0, len(arr)):
    vallr += arr[i][i] 

i = 0
for j in range(len(arr)-1, -1, -1):
    valrl += arr[i][j]
    i += 1
    
   
print(abs(vallr - valrl))
    