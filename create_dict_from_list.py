import random

vlist = ['amanda', 'mor', 'mozinho', 'feiosa', 'lindinha', 'linda', 'fidida']

mychoice = random.choices(vlist)
print(mychoice)

cities = ['Valencia', 'Munich', 'Ingolstadt']

mor_dic = dict(zip(cities,vlist))
print(mor_dic)