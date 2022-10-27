from random import vonmisesvariate
ops = ['5','2','C','D','+']
score = []
vtotal = 0
for c in ops:
    if c in '0123456789':
        score.append(c)
    elif c == 'C':
        score.pop()
    elif c == 'D':
        score.append(str(2*int(score[-1])))
    elif c == '+':
        score.append(str(int(score[-1])+int(score[-2]))) 
string = " + ".join(score)
print('The total sum is '+ string + ' = '+str(eval(string))+'.')

s = 'mauro'
print(s[:-1])