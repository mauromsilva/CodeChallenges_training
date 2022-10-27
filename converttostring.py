def vstr(pstr):
    return('str '+str(pstr))

vlist = [2, 3, 84, 2,23, 12, 11, 84, 1, 89]

# CONVERT TO STRING IN BUILT FUNCTION
print(list(map(str, vlist)))

# CONVERT TO STRING PERSONALIZED FUNCTION
print(list(map(vstr, vlist)))