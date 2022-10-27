import re
vsentence01 = 'mauro moreira silva mm!,;s'
vsentence02 = 'hoje é o melhor dia da minha vida'

for c in "!?,;.'":
    vsentence01 = vsentence01.replace(c,'')
print(vsentence01)
vwords = vsentence01.split()
print(sum(len(word) for word in vwords)/len(vwords))