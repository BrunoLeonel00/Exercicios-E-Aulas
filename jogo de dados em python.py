from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
players = list()
rankin = list()
cont = 0
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for j, v in jogo.items():
    print(f'O jogador {j} tirou {v}')
    sleep(1)
print('-------- Ranking ---------')
rankin = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for j, n in enumerate(rankin):
    print(f'{j+1} lugar {n[0]} com {n[1]} ')
