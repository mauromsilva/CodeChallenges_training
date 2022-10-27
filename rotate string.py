s = input().strip()
k = int(input().strip())
srotate = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
alphabetrotate = {}
for l in alphabet:
    if l == 'W':
        print(l)
    ordl = ord(l)+k
    if ordl > 90:
        ordl = 64 + (ordl - 90)
    alphabetrotate[l] = chr(ordl)

for c in s:
    if c.upper() in alphabet:
        if c.isupper():
            crotate = alphabetrotate[c]
        else:
            crotate = alphabetrotate[c.upper()].lower()
    else:
        crotate = c
    srotate += crotate

print(srotate)