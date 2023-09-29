import random
from time import sleep
print('---JOKEMPO---')
escolhas = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.choice(escolhas)
jogador = str(input('Qual a sua escolha ? ')).strip().upper()
print('JO')
sleep(1)
print('KE')
sleep(1)
print('PO')
print(f'Voce jogou {jogador} E o computador jogou {computador}')
sleep(1)

print('========')
if jogador == 'PEDRA' and computador == 'TESOURA':
    print('JOGADOR VENCE')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('COMPUTADOR VENCE')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('JOGADOR VENCE')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('COMPUTADOR VENCE')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('JOGADOR VENCE')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('COMPUTADOR VENCE')
else:
    print('EMPATE')