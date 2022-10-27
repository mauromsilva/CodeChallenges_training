# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

k, m = map(int, input().split())
lista = []
flist = []
maior = 0
elements = []

for _ in range(k):
    lista = list(map(int, input().split()))
    lista = lista[1:]
    flist.append(lista)
elements = [i for i in itertools.product(*flist)]   
for c in elements:
    valor = sum(list(map(lambda x: x*x, c))) % m
    if valor > maior:
        maior = valor     

print(maior)

    