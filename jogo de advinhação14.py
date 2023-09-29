'''from random import randint
print('Jogo de advinha ')
computador = randint(0, 10)
palpites = 1
jogador = int(input('Qual numero estou pensando? '))
if jogador == computador:
    print('Caramba de primeira!')
else:
    while jogador != computador:
        jogador = int(input('tente ate acertar: '))
        if jogador == computador:
            print('\033[1;34mAcertou parabens\033[m')
        elif jogador < computador:
            print('Mais')
        elif jogador > computador:
            print('Menos')
        print('-='* 10)
        palpites += 1
print(f'Voce precisou de {palpites} tentativas ')'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador, e acabei de pensar em um numero de 0 a 10')
print('Tente advinhar')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print(f'Voce acertou com {palpite} tentavas, parabens')
