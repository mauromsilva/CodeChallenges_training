def finderrornum(nums):
    previous = nums[0]
    vresult = []
    for i in range(1,len(nums)):
        # se o número atual não é igual ao anterior mais um
        # achou o duplicado mostra o atual e o que deveria ser 
        if nums[i] != (previous + 1):
            vresult.append(nums[i])
            vresult.append(previous+1)
            break
        previous = nums[i]
    return vresult

line = input()
components = line.strip().split()
components = [int(component) for component in components]
print(finderrornum(components))