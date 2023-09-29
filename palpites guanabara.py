from random import randint
from time import sleep
lista = list()
jogos = list()
print('---- JOGO DA SENA ----')
qant = int(input('Quantos jogos voce quer gerar? '))
tot = 1
while tot <= qant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('---------')
for j, p in enumerate(jogos):
    print(f'Jogo {j+1}: {p} ')
    sleep(1)