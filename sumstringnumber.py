
#OPÇÃO 01
vnum1 = '1400'
vnum2 = '100'

vtot = eval(vnum1) + eval(vnum2)
print(vtot)


# OUTRA FORMA
def solution(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10**(len(num1)-1), 10**(len(num2)-1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1 
        m1 = m1//10        

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2//10

    return str(n1 + n2)
print(solution(vnum1, vnum2))

