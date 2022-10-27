import enum


names = ['Peter', 'Clark', 'Wade', 'Bruce']
heroes = ['Spider','Super', 'Deadpool','Batman']

for index, n in enumerate(names):
    h = heroes[index]
    print(f'{n} is actually {h}')

for n, h in zip(names, heroes):
    print(f'{n} is actually {h}')