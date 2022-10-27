import re

def isPalindrome(vword):
    vwordtemp = ''.join(re.findall(r'[a-z]+', vword.lower()))
    if vwordtemp == vwordtemp[::-1]:
        return True
    return False 

vword = 'ama'
print(isPalindrome(vword))

vword = 'race car'
print(isPalindrome(vword))
