from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} ate {f} pulando de {p} em {p}')
    sleep(0.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM')


# programa principal
contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 20)
print('Sua vez de organizar a sua contagem')
ini = int(input('Inicio: '))
fim = int(input('FIM:  '))
passo = int(input('Passo: '))
contador(ini, fim, passo)