from random import randint
print('==== vamos jogar par ou impar ====')
vitorias_consecutivas = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    escolha = str(input('PAR OU IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}')
    print('-=' * 20)
    if escolha == 'P':
        if soma % 2 == 0:
            print('jogador venceu!!')
            print('Vamos jogar novamente ')
            print('=-=' * 20)
            vitorias_consecutivas += 1
        else:
            print('Computador venceu!!')
            print('=-=' * 20)
            break
    elif escolha == 'I':
        if soma % 2 != 0:
            print('Jogador venceu!!!')
            print('=-=' * 20)
            vitorias_consecutivas += 1
        else:
            print('Computador vence!!!')
            print('=-=' * 20)
            break
if vitorias_consecutivas >= 2:
    print(f'Parabens teve {vitorias_consecutivas} vitorias seguidas ')
else:
    print(f'Puts, nao deu pra voce mesmo.')