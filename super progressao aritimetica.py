'''primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
while cont < 10:
    print(f'{primeiro_termo}', end='-> ')
    primeiro_termo += razao
    cont += 1
    if cont == 10:
        n = int(input('\nDeseja mostrar quantos termos? '))
        print('=' * 20)
        while n != 0:
            for c in range(0, n):
                print(f'{primeiro_termo}', end='->')
                primeiro_termo += razao
            print('-=' * 20)
            n = int(input('Deseja mostrar mais qunatos ?'))
print('ACABOU')'''
print('Gerador de P.a')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao: '))
termo = primeiro  # numero inicial
cont = 0
mais = 10        # como é uma p.a e temos que mostrar os 10 primeiros termos, a variavel mais ja inicia com o valor 10
total = 0        # total de termos mostrados
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ', end='->')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Deseja mostrar quantos termos a mais? '))
print(f'Progressao finalizada com {total} termos mostrados')