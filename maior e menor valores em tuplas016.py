from random import randint
numeros_aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print(numeros_aleatorios)
print(f'O menor valor da lista é {sorted(numeros_aleatorios)[0]}')
print(f'O maior valor da lista é {sorted(numeros_aleatorios)[-1]}') # podemos fazer assim, ou podemos usar a função MAX e MIN
