from time import sleep
from random import randint

numeros = list()


def sortear():
    print('Sorteando 5 valores: ', end=' ')
    for n in range(0, 5):
        n = randint(0, 10)
        print(f'{n}', end=' ')
        numeros.append(n)
    print('pronto!')


def somarPar():
    par = 0
    for c in numeros:
        if c % 2 == 0:
            par += c
    print(f'Somando os valores {numeros} temos {par}')


sortear()
somarPar()