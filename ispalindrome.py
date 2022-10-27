def isPalindrome(vword):
    vwordtemp = vword
    if vwordtemp == vwordtemp[::-1]:
        return True

    for vletter in vword:
        vwordtemp = vword
        vwordtemp = vwordtemp.replace(vletter,'')
        if vwordtemp == vwordtemp[::-1]:
            return True 
            break
    return False 

vword = 'aema1'
print(isPalindrome(vword))

vword = 'ama1'
print(isPalindrome(vword))
