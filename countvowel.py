import re
def countvowel(vword):
    vwordtemp = ''.join(re.findall(r'[aeiou]+',vword.lower()))
    print(vwordtemp)


countvowel('mauro moreira silva')