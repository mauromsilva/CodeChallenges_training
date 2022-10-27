thickness = 5
c = 'H'

#Top Cone
vtam = (thickness-1)*2+1
for i in range(thickness):
    vstr = c+(c*i)*2
    print(vstr.center(vtam, ' '))

#Top Pillars
for i in range(thickness+1):
    print(  (c*thickness).center(thickness*2,' ')
            +
            (c*thickness).center(thickness*6, ' ')
    )

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6, ' '))    


#Bottom Pillars
for i in range(thickness+1):
    print(  (c*thickness).center(thickness*2,' ')
            +
            (c*thickness).center(thickness*6, ' ')
    )

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness,' ')+
        c+
        (c*(thickness-i-1)).ljust(thickness, ' ') 
        ).rjust(thickness*6, ' '))