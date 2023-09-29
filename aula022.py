def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# programa principal
num = int(input('Digite um numero: '))
fat = fatorial(num)
print(f'O fatorail de {num} é {fat}')
