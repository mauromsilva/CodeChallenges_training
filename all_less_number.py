vnumber = 89
vlist = [2, 3, 84, 2,23, 12, 11, 84, 1, 89]

print(all(i < vnumber for i in vlist ))

# ORDER A LIST STRING LENGTH DESCENDNG
vwords = sorted(['mama valencia', 'toronto', 'madri', 'san diego'], key=len, reverse=True)
print(vwords)

# ORDER DESCENDING ALPHABETIC
vwords = sorted(vwords, reverse=True)
print(vwords)

# ORDER A DICTIONARY
vdicwords = {'Mauro':1, 'Amanda':2, 'Felipe':3}

# SORTED BY KEY
print({key: vdicwords[key] for key in sorted(vdicwords)})

# SORTED BY VALUE
print({key: vdicwords[key] for key in sorted(vdicwords, key=vdicwords.get)})
