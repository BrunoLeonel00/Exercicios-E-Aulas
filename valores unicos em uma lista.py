lista_numeros = list()
while True:
    n = int(input('Digite varios numeros: '))
    if n not in lista_numeros:
        lista_numeros.append(n)
    else:
        print('Valores repetidos nao pode')
    op = str(input('Deseja continuar? ')).strip().upper()[0]
    if op == 'N':
        break
lista_numeros.sort()
print(f'A lista dos numeros adicionados em ordem crescente {lista_numeros}')
