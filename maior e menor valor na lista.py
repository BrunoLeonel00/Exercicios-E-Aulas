maior = menor = 0
lista_numeros = list()
for c in range(0, 5):
    lista_numeros.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = lista_numeros[c]
    else:
        if lista_numeros[c] > maior:
            maior = lista_numeros[c]
        if lista_numeros[c] < menor:
            menor = lista_numeros[c]
print('-------')
print(f'Você digitou os valores: {lista_numeros}')
print(f"O maior valor digitado na lista é {maior} ", end='')
print('Nas posições', end='')
for pos, v in enumerate(lista_numeros):
    if v == maior:
        print(f' {pos}', end='... ')
print(f'\no menor valor digitado é {menor} ', end='')
print('Nas posições', end='')
for pos, v in enumerate(lista_numeros):
    if v == menor:
        print(f' {pos}', end='...')
