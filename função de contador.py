from time import sleep


def lin():
    print('~~' * 15)


def contador(i, f, p):

    for c in range(i, f, p):
        print(f'{c}', end=' ')
        if c == f:
            print('FIM')

    print()


# Programa principal
lin()
print('Contagem de 1 até 10 pulando de 1 em 1')
contador(1, 11, 1)
lin()
print('Contagem de 10 até 0, pulando de 2 em 2')
contador(10, -1, -2)
lin()
print('Agora é sua vez de personalizar a sua contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
lin()
if passo < 0:
    passo *= -1
if passo == 0:
    passo = 1
print(f'Contagem de {inicio} até {fim} pulando de {passo}')
contador(inicio, fim, passo)
