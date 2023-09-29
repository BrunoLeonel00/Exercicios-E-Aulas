from random import randint
from time import sleep
palpites = [[], [], [], [], [], []]
cont = pos = 0
n = int(input('Quantos jogos serão gerados? '))
for j in range(0, n):
    if n > 6:
        palpites.append([])
    for p in range(0, 6):
        if palpites[p] not in palpites[j]:
            palpites[j].append(randint(0, 60))
    palpites[j].sort()
    print(f'Jogo {j+1}: {palpites[j]}')
    sleep(1)
print()
print(f'{"Boa Sorte":=^30}')

